# Neon-API-Tester/ui/app.py

import customtkinter as ctk
from ui.colors import Palette
from ui.fonts import load_fonts, load_image
from ui.components.request_panel import RequestPanel
from ui.components.response_panel import ResponsePanel
from ui.components.history_panel import HistoryPanel


class App(ctk.CTk):
    """The main application window that assembles all UI components."""

    def __init__(self, rerun_callback):
        super().__init__()

        self.fonts = load_fonts()
        self.rerun_callback = rerun_callback

        self.title("⚡ Neon API Tester")
        self.geometry("1280x850")

        self.bg_image = load_image(
            "assets/images/background.png", size=(2000, 1200))
        if self.bg_image:
            self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=0)

        self.header = ctk.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.header.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.logo_label = ctk.CTkLabel(self.header, text="⚡ NEON API", font=self.fonts["title"],
                                       text_color=(Palette.LIGHT_PRIMARY, Palette.PRIMARY_CYAN))  # <-- MODIFIED
        self.logo_label.pack(side="left")

        self.theme_switch = ctk.CTkSwitch(self.header, text="Dark Mode", font=self.fonts["body"],
                                          progress_color=Palette.SECONDARY_MAGENTA,
                                          text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT))  # <-- MODIFIED
        self.theme_switch.pack(side="right", padx=10)

        self.analytics_button = ctk.CTkButton(self.header, text="Analytics", font=self.fonts["heading"],
                                              fg_color=(
                                                  Palette.LIGHT_PRIMARY, "#3b82f6"),
                                              hover_color=(Palette.LIGHT_SECONDARY, "#2563eb"))
        self.analytics_button.pack(side="right", padx=10)

        self.history_toggle_button = ctk.CTkButton(self.header, text="History", font=self.fonts["heading"],
                                                   command=self.toggle_history,
                                                   # <-- NEW
                                                   fg_color=(
                                                       Palette.LIGHT_PRIMARY, "#3b82f6"),
                                                   hover_color=(Palette.LIGHT_SECONDARY, "#2563eb"))  # <-- NEW
        self.history_toggle_button.pack(side="right", padx=10)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=1, column=0, padx=20,
                             pady=(0, 10), sticky="nsew")
        self.main_frame.grid_columnconfigure((0, 1), weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.request_panel = RequestPanel(self.main_frame, self.fonts)
        self.request_panel.grid(row=0, column=0, padx=(0, 10), sticky="nsew")
        self.response_panel = ResponsePanel(self.main_frame, self.fonts)
        self.response_panel.grid(row=0, column=1, padx=(10, 0), sticky="nsew")

        self.history_panel = HistoryPanel(
            self, self.fonts, self.rerun_callback)
        self.history_visible = False

    def set_theme(self, mode):
        """Sets the application theme and safely handles the background image."""
        ctk.set_appearance_mode(mode)

        if hasattr(self, 'bg_label') and self.bg_label:
            if mode == "Dark":
                self.bg_label.configure(image=self.bg_image)
                # Ensure it's visible
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            else:
                self.bg_label.place_forget()  # Hide it completely in light mode
        # --- END OF FIX ---

        if mode == "Dark":
            self.theme_switch.select()
        else:
            self.theme_switch.deselect()

    def toggle_history(self):
        if self.history_visible:
            self.history_panel.grid_forget()
            self.grid_rowconfigure(1, weight=5)
            self.grid_rowconfigure(2, weight=0)
            self.history_visible = False
        else:
            self.history_panel.grid(
                row=2, column=0, padx=20, pady=10, sticky="nsew")
            self.grid_rowconfigure(1, weight=4)
            self.grid_rowconfigure(2, weight=2)
            self.history_visible = True
