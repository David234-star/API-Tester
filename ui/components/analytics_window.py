# Neon-API-Tester/ui/components/analytics_window.py (Corrected)

import customtkinter as ctk
from ui.colors import Palette
from utils.analytics_calculator import AnalyticsCalculator
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.font_manager as fm  # <-- IMPORT FONT MANAGER
import os  # <-- IMPORT OS

# --- FIX IS HERE: Register our custom font with Matplotlib ---
font_path = os.path.join("assets", "fonts", "Orbitron-VariableFont_wght.ttf")
if os.path.exists(font_path):
    fm.fontManager.addfont(font_path)
    # You can optionally set the rcParams to use Orbitron by default in plots
    # matplotlib.rcParams['font.family'] = 'Orbitron'
# --- END OF FIX ---


class AnalyticsWindow(ctk.CTkToplevel):
    """A popup window to display API request analytics."""

    def __init__(self, master, analytics_data, fonts):
        # ... (The rest of the __init__ method is EXACTLY the same as the previous correct version) ...
        super().__init__(master)
        self.title("⚡ API Analytics")
        self.geometry("700x550")
        self.fonts = fonts
        self.calculator = AnalyticsCalculator(analytics_data)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        endpoints = ["Overall Summary"] + self.calculator.get_endpoints()
        self.endpoint_var = ctk.StringVar(value=endpoints[0])
        self.endpoint_menu = ctk.CTkOptionMenu(
            header_frame, variable=self.endpoint_var, values=endpoints,
            font=self.fonts["body"], command=self.update_display,
            fg_color=(Palette.LIGHT_BACKGROUND, Palette.DARK_BACKGROUND),
            text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT),
            button_color=(Palette.LIGHT_SECONDARY, Palette.SECONDARY_MAGENTA)
        )
        self.endpoint_menu.pack(fill="x")

        self.stats_frame = ctk.CTkFrame(self, fg_color=(
            Palette.LIGHT_CARD_BG, Palette.DARK_CARD_BG))
        self.stats_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.stats_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.total_req_label_value, total_req_frame = self._create_stat_widget(
            "Total Requests")
        self.avg_time_label_value, avg_time_frame = self._create_stat_widget(
            "Avg Time (ms)")
        self.min_time_label_value, min_time_frame = self._create_stat_widget(
            "Min Time (ms)")
        self.max_time_label_value, max_time_frame = self._create_stat_widget(
            "Max Time (ms)")
        self.avg_size_label_value, avg_size_frame = self._create_stat_widget(
            "Avg Size (bytes)")

        total_req_frame.grid(row=0, column=0, padx=10, pady=10)
        avg_time_frame.grid(row=0, column=1, padx=10, pady=10)
        min_time_frame.grid(row=0, column=2, padx=10, pady=10)
        max_time_frame.grid(row=0, column=3, padx=10, pady=10)
        avg_size_frame.grid(row=0, column=4, padx=10, pady=10)

        self.chart_frame = ctk.CTkFrame(self, fg_color=(
            Palette.LIGHT_CARD_BG, Palette.DARK_CARD_BG))
        self.chart_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.fig = Figure(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)

        self.update_display()

    def _create_stat_widget(self, title):
        frame = ctk.CTkFrame(self.stats_frame, fg_color="transparent")
        ctk.CTkLabel(frame, text=title, font=self.fonts["code"], text_color=(
            Palette.LIGHT_BORDER, Palette.DARK_BORDER)).pack()
        value_label = ctk.CTkLabel(
            frame, text="---", font=self.fonts["heading"], text_color=(Palette.LIGHT_TEXT, Palette.DARK_TEXT))
        value_label.pack()
        return value_label, frame

    def update_display(self, selected_endpoint=None):
        if selected_endpoint is None:
            selected_endpoint = self.endpoint_var.get()
        stats = self.calculator.get_summary_stats(
        ) if selected_endpoint == "Overall Summary" else self.calculator.get_stats_for_endpoint(selected_endpoint)
        self.total_req_label_value.configure(
            text=f"{stats['total_requests']:,}")
        self.avg_time_label_value.configure(text=f"{stats['avg_time']:.2f}")
        self.min_time_label_value.configure(text=f"{stats['min_time']:.2f}")
        self.max_time_label_value.configure(text=f"{stats['max_time']:.2f}")
        self.avg_size_label_value.configure(text=f"{stats['avg_size']:,.0f}")
        self.draw_status_chart(stats["status_code_distribution"])

    def draw_status_chart(self, distribution):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        codes = sorted(distribution.keys())
        counts = [distribution[c] for c in codes]
        is_dark = ctk.get_appearance_mode() == "Dark"
        bar_colors = [("#008000" if str(c).startswith('2')
                       else "#CC0000") for c in codes]
        text_color = Palette.DARK_TEXT if is_dark else Palette.LIGHT_TEXT
        bg_color = Palette.DARK_CARD_BG if is_dark else Palette.LIGHT_CARD_BG
        self.fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        ax.tick_params(colors=text_color)
        ax.spines['bottom'].set_color(text_color)
        ax.spines['left'].set_color(text_color)
        ax.spines['top'].set_color(bg_color)
        ax.spines['right'].set_color(bg_color)

        # Tell this specific title to use the font
        ax.set_title("Status Code Distribution",
                     color=text_color, fontname='Orbitron')

        if not codes:
            ax.text(0.5, 0.5, "No Data", ha='center',
                    va='center', color=text_color)
        else:
            ax.bar([str(c) for c in codes], counts, color=bar_colors)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both",
                                         expand=True, padx=10, pady=10)
