

class Palette:
    """Retro-Futuristic Neon Color Palette"""
    # --- UNIVERSAL ---
    PRIMARY_CYAN = "#7DF9FF"
    SECONDARY_MAGENTA = "#FF00FF"

    # --- DARK THEME ---
    DARK_BACKGROUND = "#0A0A1A"
    DARK_CARD_BG = "#141426"
    DARK_TEXT = "#E0E0FF"
    DARK_BORDER = "#4A4A6A"

    # --- LIGHT THEME (High Contrast) ---
    LIGHT_BACKGROUND = "#E0E0FF"
    LIGHT_CARD_BG = "#F0F0FF"
    LIGHT_TEXT = "#0A0A1A"  # Black for text
    LIGHT_BORDER = "#B0B0D0"
    LIGHT_PRIMARY = "#006B70"  # Dark Cyan for buttons/accents
    LIGHT_SECONDARY = "#990099"  # Dark Magenta for buttons/accents

    # --- STATUS COLORS (Now Theme-Aware) ---
    SUCCESS = ("#008000", "#00FF7F")  # (LightMode, DarkMode)
    ERROR = ("#CC0000", "#FF4500")   # (LightMode, DarkMode)

    # --- SYNTAX HIGHLIGHTING (for Dark Mode) ---
    SYNTAX_KEYWORD = "#FF00FF"
    SYNTAX_STRING = "#7DF9FF"
    SYNTAX_NUMBER = "#FFD700"
    SYNTAX_BRACKET = "#E0E0FF"
