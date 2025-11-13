# Neon-API-Tester/ui/fonts.py

import customtkinter as ctk
from PIL import Image
import os


def load_fonts():
    """Loads and registers custom fonts for the application."""
    try:
        ctk.FontManager.load_font(
            "assets\\fonts\\Orbitron-VariableFont_wght.ttf")
        ctk.FontManager.load_font(
            "assets\\fonts\\VT323-Regular.ttf")
        return {
            "title": ("Orbitron", 28, "bold"),
            "heading": ("Orbitron", 16, "bold"),
            "body": ("VT323", 18),
            "code": ("Roboto Mono", 13),
            "history": ("VT323", 16)
        }
    except Exception as e:
        print(f"Error loading fonts: {e}. Using default system fonts.")
        return {
            "title": ("Arial", 28, "bold"),
            "heading": ("Arial", 16, "bold"),
            "body": ("Arial", 14),
            "code": ("Courier New", 12),
            "history": ("Arial", 12)
        }


def load_image(path, size=(24, 24)):
    """Loads a CTkImage from a path, handling potential errors."""
    if os.path.exists(path):
        return ctk.CTkImage(Image.open(path), size=size)
    print(f"Warning: Image not found at path: {path}")
    return None
