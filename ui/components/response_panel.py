# Neon-API-Tester/ui/components/response_panel.py

import customtkinter as ctk
from ui.colors import Palette
from .syntax_highlighter import SyntaxHighlighter


class ResponsePanel(ctk.CTkFrame):
    def __init__(self, master, fonts):
        super().__init__(master, corner_radius=12)
        self.fonts = fonts
        self.configure(fg_color=(Palette.LIGHT_CARD_BG, Palette.DARK_CARD_BG))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.info_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.info_frame.grid(row=0, column=0, columnspan=2,
                             padx=10, pady=10, sticky="ew")

        self.status_label = ctk.CTkLabel(self.info_frame, text="Status: ---", font=self.fonts["body"],
                                         text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT))  # <-- MODIFIED
        self.status_label.pack(side="left", padx=5)
        self.time_label = ctk.CTkLabel(self.info_frame, text="Time: --- ms", font=self.fonts["body"],
                                       text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT))  # <-- MODIFIED
        self.time_label.pack(side="left", padx=5)

        self.export_button = ctk.CTkButton(
            self.info_frame, text="Export", font=self.fonts["heading"],
            fg_color="transparent", border_width=1,
            border_color=(Palette.LIGHT_BORDER, Palette.DARK_BORDER),
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            hover_color=(Palette.LIGHT_PRIMARY, Palette.PRIMARY_CYAN), width=80
        )  # <-- MODIFIED BLOCK
        self.export_button.pack(side="right", padx=5)

        self.response_textbox = ctk.CTkTextbox(
            self, font=self.fonts["code"], corner_radius=8, border_width=1,
            border_color=(Palette.LIGHT_BORDER, Palette.DARK_BORDER),
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            wrap="word", fg_color=(Palette.LIGHT_BACKGROUND, "#050510")
        )  # <-- MODIFIED BLOCK
        self.response_textbox.grid(
            row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.highlighter = SyntaxHighlighter(self.response_textbox)

    def display_response(self, status_code, response_time, response_json):
        self.response_textbox.configure(state="normal")
        self.response_textbox.delete("1.0", "end")
        self.response_textbox.insert("1.0", response_json)
        # Only highlight in dark mode, as colors are tuned for it
        if ctk.get_appearance_mode() == "Dark":
            self.highlighter.highlight()
        self.response_textbox.configure(state="disabled")

        status_color = Palette.SUCCESS if 200 <= status_code < 300 else Palette.ERROR
        self.status_label.configure(
            text=f"Status: {status_code}", text_color=status_color)
        self.time_label.configure(text=f"Time: {response_time:.2f} ms")

    def get_content(self):
        return self.response_textbox.get("1.0", "end-1c")
