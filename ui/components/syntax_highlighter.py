# Neon-API-Tester/ui/components/syntax_highlighter.py

from pygments import lex
from pygments.lexers import JsonLexer
from pygments.token import Token
from ui.colors import Palette
import time


class SyntaxHighlighter:
    """Applies color tags to text in a CTkTextbox based on JSON syntax."""

    def __init__(self, textbox):
        self.textbox = textbox
        self.lexer = JsonLexer()

        self.tag_map = {
            Token.Keyword: Palette.SYNTAX_KEYWORD,
            Token.Name.Tag: Palette.SYNTAX_KEYWORD,
            Token.Literal.String.Double: Palette.SYNTAX_STRING,
            Token.Literal.Number.Integer: Palette.SYNTAX_NUMBER,
            Token.Literal.Number.Float: Palette.SYNTAX_NUMBER,
            Token.Punctuation: Palette.SYNTAX_BRACKET,
            Token.Operator: Palette.SYNTAX_BRACKET,
        }
        self._configure_tags()

    def _configure_tags(self):
        """Sets up the tag configurations in the textbox."""
        for token_type, color in self.tag_map.items():
            self.textbox.tag_config(str(token_type), foreground=color)

    def highlight(self):
        """Lexes the content and applies syntax highlighting tags."""
        text = self.textbox.get("1.0", "end-1c")
        if not text:
            return

        # Clear all previous tags to prevent overlap
        for tag in self.textbox.tag_names():
            if tag != "sel":
                self.textbox.tag_remove(tag, "1.0", "end")

        # Apply new tags based on tokenization
        start_pos = 0
        for token, content in lex(text, self.lexer):
            start_index = f"1.0 + {start_pos} chars"
            end_index = f"{start_index} + {len(content)} chars"

            if token in self.tag_map:
                self.textbox.tag_add(str(token), start_index, end_index)

            start_pos += len(content)
