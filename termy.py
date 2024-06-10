import pyfiglet
from termcolor import colored

class Termy:
    @staticmethod
    def head_text(text, font="slant", color="white", on_color=None, attrs=None):
        figlet = pyfiglet.Figlet(font=font)
        ascii_art = figlet.renderText(text)
        colored_art = colored(ascii_art, color=color, on_color=on_color, attrs=attrs)
        print(colored_art)

    @staticmethod
    def link(url, link_text, color="blue", on_color=None, attrs=None):
        colored_link_text = colored(link_text, color=color, on_color=on_color, attrs=attrs)
        print(f"\033]8;;{url}\033\\{colored_link_text}\033]8;;\033\\")
