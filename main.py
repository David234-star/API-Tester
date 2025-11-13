# Neon-API-Tester/main.py

from ui.app import App
from utils.storage import load_data, save_data
from ui.components.analytics_window import AnalyticsWindow
import requests
import time
import json
import validators
from tkinter import messagebox, filedialog
from datetime import datetime


class MainApp(App):
    """The main controller class that handles application logic."""

    def __init__(self):
        self.app_data = load_data()
        super().__init__(rerun_callback=self.rerun_request)

        # Configure theme from saved settings
        initial_theme = self.app_data.get("settings", {}).get("theme", "Dark")
        self.set_theme(initial_theme)

        # Connect UI commands to logic
        self.theme_switch.configure(command=self.toggle_and_save_theme)
        self.request_panel.send_button.configure(command=self.send_api_request)
        self.response_panel.export_button.configure(
            command=self.export_response)

        self.load_history_into_ui()
        self.analytics_button.configure(command=self.open_analytics_window)

    def toggle_and_save_theme(self):
        mode = "Dark" if self.theme_switch.get() else "Light"
        self.set_theme(mode)
        self.app_data.setdefault("settings", {})["theme"] = mode
        save_data(self.app_data)

    def load_history_into_ui(self):
        for item in self.app_data.get("history", []):
            self.history_panel.add_history_item(item, at_top=False)

    def rerun_request(self, history_item):
        self.request_panel.method_var.set(history_item.get("method", "GET"))
        self.request_panel.url_entry.delete(0, "end")
        self.request_panel.url_entry.insert(0, history_item.get("url", ""))

        headers_str = json.dumps(history_item.get("headers", {}), indent=2)
        self.request_panel.headers_textbox.delete("1.0", "end")
        self.request_panel.headers_textbox.insert("1.0", headers_str)

        body_str = json.dumps(history_item.get("body", {}), indent=2)
        self.request_panel.body_textbox.delete("1.0", "end")
        self.request_panel.body_textbox.insert("1.0", body_str)

        self.send_api_request(add_to_history=False)

    def export_response(self):
        content = self.response_panel.get_content()
        if not content.strip():
            messagebox.showwarning(
                "Export Empty", "There is no response content to export.")
            return

        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"),
                       ("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Response As"
        )
        if filepath:
            try:
                with open(filepath, 'w') as f:
                    f.write(content)
                messagebox.showinfo(
                    "Export Success", f"Response saved to {filepath}")
            except Exception as e:
                messagebox.showerror(
                    "Export Error", f"Could not save file: {e}")

    def open_analytics_window(self):
        """Creates and shows the analytics toplevel window."""
        analytics_data = self.app_data.get("analytics", {})
        AnalyticsWindow(self, analytics_data, self.fonts)

    def send_api_request(self, add_to_history=True):
        url = self.request_panel.url_entry.get()
        if not validators.url(url):
            messagebox.showerror("Invalid URL", "Please enter a valid URL.")
            return

        method = self.request_panel.method_var.get()
        try:
            headers = json.loads(
                self.request_panel.headers_textbox.get("1.0", "end") or '{}')
            body = json.loads(
                self.request_panel.body_textbox.get("1.0", "end") or '{}')
        except json.JSONDecodeError as e:
            messagebox.showerror(
                "Invalid JSON", f"Please check your Headers/Body formatting.\n{e}")
            return

        try:
            start_time = time.time()
            response = requests.request(
                method=method, url=url, headers=headers, json=body, timeout=10)
            response_time = (time.time() - start_time) * 1000

            try:
                response_formatted = json.dumps(response.json(), indent=2)
            except json.JSONDecodeError:
                response_formatted = response.text

            self.response_panel.display_response(
                response.status_code, response_time, response_formatted)

            endpoint_key = f"{method} {url.split('?')[0]}"
            analytics_entry = {
                "timestamp": datetime.now().isoformat(),
                "status_code": response.status_code,
                "response_time_ms": response_time,
                "response_size_bytes": len(response.content)
            }
            # Initialize data structures if they don't exist
            self.app_data.setdefault("analytics", {})
            self.app_data["analytics"].setdefault(
                endpoint_key, []).append(analytics_entry)

            if add_to_history:
                history_item = {
                    "method": method, "url": url, "headers": headers, "body": body,
                    "status_code": response.status_code, "timestamp": datetime.now().isoformat()
                }
                self.app_data["history"].append(history_item)
                save_data(self.app_data)
                self.history_panel.add_history_item(history_item, at_top=True)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Request Error", f"An error occurred: {e}")
            self.response_panel.display_response(0, 0, str(e))


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
