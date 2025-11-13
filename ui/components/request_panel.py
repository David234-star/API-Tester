# Neon-API-Tester/ui/components/request_panel.py

import customtkinter as ctk
from ui.colors import Palette


class RequestPanel(ctk.CTkFrame):
    """The left panel containing all request building UI elements."""

    def __init__(self, master, fonts):
        super().__init__(master, corner_radius=12)
        self.fonts = fonts
        self.configure(fg_color=(Palette.LIGHT_CARD_BG, Palette.DARK_CARD_BG))

        self.grid_columnconfigure(1, weight=1)

        self.method_var = ctk.StringVar(value="GET")
        self.method_menu = ctk.CTkOptionMenu(
            self, values=["GET", "POST", "PUT", "DELETE", "PATCH"],
            variable=self.method_var, font=self.fonts["body"],
            fg_color=(Palette.LIGHT_BACKGROUND, Palette.DARK_BACKGROUND),
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            button_color=(Palette.LIGHT_SECONDARY, Palette.SECONDARY_MAGENTA),
            button_hover_color=(Palette.LIGHT_PRIMARY, Palette.PRIMARY_CYAN),
            dropdown_fg_color=(Palette.LIGHT_CARD_BG, Palette.DARK_CARD_BG),
            dropdown_text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            corner_radius=8
        )  # <-- MODIFIED BLOCK
        self.method_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.url_entry = ctk.CTkEntry(
            self, placeholder_text="Enter API URL here...", font=self.fonts["body"],
            corner_radius=8, border_width=1, border_color=Palette.PRIMARY_CYAN,
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            placeholder_text_color=(Palette.LIGHT_BORDER, Palette.DARK_BORDER),
            fg_color=(Palette.LIGHT_BACKGROUND, Palette.DARK_BACKGROUND)
        )  # <-- MODIFIED BLOCK
        self.url_entry.grid(row=0, column=1, padx=(0, 10),
                            pady=10, sticky="ew")

        self.tab_view = ctk.CTkTabview(self, corner_radius=8,
                                       border_color=(
                                           Palette.LIGHT_BORDER, Palette.DARK_BORDER),
                                       fg_color="transparent",  # Let the textboxes handle color
                                       segmented_button_selected_color=(
                                           Palette.LIGHT_SECONDARY, Palette.SECONDARY_MAGENTA),
                                       segmented_button_selected_hover_color=(
                                           Palette.LIGHT_PRIMARY, Palette.PRIMARY_CYAN),
                                       segmented_button_unselected_color=(
                                           Palette.LIGHT_CARD_BG, Palette.DARK_CARD_BG),
                                       text_color_disabled=(
                                           Palette.LIGHT_BORDER, Palette.DARK_BORDER),
                                       text_color=(
                                           Palette.LIGHT_TEXT, Palette.DARK_TEXT),
                                       border_width=1)  # <-- MODIFIED BLOCK
        self.tab_view.add("Headers")
        self.tab_view.add("Body (JSON)")
        self.tab_view.grid(row=1, column=0, columnspan=2,
                           padx=10, pady=5, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)

        self.headers_textbox = ctk.CTkTextbox(
            self.tab_view.tab("Headers"), font=self.fonts["code"], wrap="word",
            corner_radius=8, border_width=1, border_color=(Palette.LIGHT_BORDER, Palette.DARK_BORDER),
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            # slightly lighter dark bg
            fg_color=(Palette.LIGHT_BACKGROUND, "#050510")
        )  # <-- MODIFIED BLOCK
        self.headers_textbox.pack(expand=True, fill="both", padx=5, pady=5)
        self.headers_textbox.insert(
            "0.0", '{\n  "Authorization": "Bearer YOUR_TOKEN"\n}')

        self.body_textbox = ctk.CTkTextbox(
            self.tab_view.tab("Body (JSON)"), font=self.fonts["code"], wrap="word",
            corner_radius=8, border_width=1, border_color=(Palette.LIGHT_BORDER, Palette.DARK_BORDER),
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            fg_color=(Palette.LIGHT_BACKGROUND, "#050510")
        )  # <-- MODIFIED BLOCK
        self.body_textbox.pack(expand=True, fill="both", padx=5, pady=5)
        self.body_textbox.insert("0.0", '{\n  "key": "value"\n}')

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10, sticky="e")

        self.send_button = ctk.CTkButton(
            self.button_frame, text="⚡ Send Request", font=self.fonts["heading"],
            fg_color=(Palette.LIGHT_PRIMARY, Palette.PRIMARY_CYAN),
            hover_color=(Palette.LIGHT_SECONDARY, Palette.SECONDARY_MAGENTA),
            text_color=(Palette.LIGHT_CARD_BG, Palette.DARK_BACKGROUND)
        )  # <-- MODIFIED BLOCK
        self.send_button.pack(side="right", padx=5)
