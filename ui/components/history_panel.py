# Neon-API-Tester/ui/components/history_panel.py

import customtkinter as ctk
from ui.colors import Palette


class HistoryPanel(ctk.CTkScrollableFrame):
    def __init__(self, master, fonts, rerun_callback):
        super().__init__(master, label_text="Request History", label_font=fonts["heading"],
                         fg_color=(Palette.LIGHT_CARD_BG,
                                   Palette.DARK_CARD_BG),
                         label_text_color=(Palette.LIGHT_TEXT,
                                           Palette.DARK_TEXT),
                         corner_radius=12)  # <-- MODIFIED BLOCK
        self.fonts = fonts
        self.rerun_callback = rerun_callback
        self._scrollbar.configure(height=0)

    def add_history_item(self, item_data, at_top=True):
        item_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=1,
                                  border_color=(
                                      Palette.LIGHT_BORDER, Palette.DARK_BORDER),
                                  corner_radius=8)  # <-- MODIFIED

        method = item_data.get('method', 'N/A')
        status = item_data.get('status_code', 'N/A')
        status_color = Palette.SUCCESS if str(
            status).startswith('2') else Palette.ERROR

        method_label = ctk.CTkLabel(item_frame, text=method, font=self.fonts["history"], width=60,
                                    text_color=(Palette.LIGHT_PRIMARY, Palette.PRIMARY_CYAN))  # <-- MODIFIED
        method_label.pack(side="left", padx=5)

        url_label = ctk.CTkLabel(item_frame, text=item_data.get('url', ''), font=self.fonts["code"],
                                 anchor="w", wraplength=500,
                                 text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT))  # <-- MODIFIED
        url_label.pack(side="left", padx=5, fill="x", expand=True)

        status_label = ctk.CTkLabel(item_frame, text=str(status), font=self.fonts["history"],
                                    width=40, text_color=status_color)  # <-- MODIFIED
        status_label.pack(side="left", padx=5)

        rerun_button = ctk.CTkButton(
            item_frame, text="Re-run", width=60, font=self.fonts["heading"],
            fg_color="transparent", border_width=1,
            border_color=(Palette.LIGHT_BORDER, Palette.DARK_BORDER),
            hover_color=(Palette.LIGHT_SECONDARY, Palette.SECONDARY_MAGENTA),
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            command=lambda data=item_data: self.rerun_callback(data)
        )  # <-- MODIFIED BLOCK
        rerun_button.pack(side="right", padx=5, pady=5)

        if at_top:
            item_frame.pack(fill="x", padx=5, pady=(5, 0), before=self._parent_canvas.winfo_children()[
                            2] if len(self._parent_canvas.winfo_children()) > 2 else None)
        else:
            item_frame.pack(fill="x", padx=5, pady=5)
