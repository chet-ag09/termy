import pyfiglet
from termcolor import colored
import re

class Termy:
    @staticmethod
    def head_text(text, font="slant", color="white", on_color=None, style=None):
        figlet = pyfiglet.Figlet(font=font)
        ascii_art = figlet.renderText(text)
        colored_art = colored(ascii_art, color=color, on_color=on_color, attrs=style)
        print(colored_art)

    @staticmethod
    def link(url, link_text, color="blue", on_color=None, style=None):
        colored_link_text = colored(link_text, color=color, on_color=on_color, attrs=style)
        print(f"\033]8;;{url}\033\\{colored_link_text}\033]8;;\033\\")

    @staticmethod
    def __render_markdown(text):
        text = re.sub(r'^(#{1}) (.*)', lambda m: colored(f'{m.group(2)}', 'red', attrs=['bold']), text, flags=re.MULTILINE)
        text = re.sub(r'^(#{2}) (.*)', lambda m: colored(f'{m.group(2)}', 'yellow', attrs=['bold']), text, flags=re.MULTILINE)
        text = re.sub(r'^(#{3}) (.*)', lambda m: colored(f'{m.group(2)}', 'green', attrs=['bold']), text, flags=re.MULTILINE)
        text = re.sub(r'^(#{4}) (.*)', lambda m: colored(f'{m.group(2)}', 'cyan', attrs=['bold']), text, flags=re.MULTILINE)
        text = re.sub(r'^(#{5}) (.*)', lambda m: colored(f'{m.group(2)}', 'blue', attrs=['bold']), text, flags=re.MULTILINE)
        text = re.sub(r'^(#{6}) (.*)', lambda m: colored(f'{m.group(2)}', 'magenta', attrs=['bold']), text, flags=re.MULTILINE)
        text = re.sub(r'\*\*(.*?)\*\*', lambda m: colored(m.group(1), attrs=['bold']), text)
        text = re.sub(r'\*(.*?)\*', lambda m: colored(m.group(1), attrs=['italic']), text)
        text = re.sub(r'^\* (.*)', lambda m: colored(f'- {m.group(1)}', 'white'), text, flags=re.MULTILINE)
        text = re.sub(r'^\d+\. (.*)', lambda m: colored(f'{m.group(0)}', 'white'), text, flags=re.MULTILINE)
        text = re.sub(r'^> (.*)', lambda m: colored(f'{m.group(0)}', 'blue', attrs=['dark']), text, flags=re.MULTILINE)

        return text

    @staticmethod
    def use_file(file_path, box_color="white"):
        with open(file_path, 'r') as f:
            content = f.read()
            # Render markdown
            rendered_content = Termy.__render_markdown(content)
            # Print content in a box with specified color
            Termy.print_box(rendered_content, box_color)

    @staticmethod
    def print_box(content, box_color):
        lines = content.split('\n')
        max_length = max(len(line) for line in lines)
        print(f'╔{colored("═" * (max_length + 2), color=box_color)}╗')
        for line in lines:
            print(f'║ {line.ljust(max_length)} ║')
        print(f'╚{colored("═" * (max_length + 2), color=box_color)}╝')


if __name__ == "__main__":
    Termy.head_text('Termy', color="blue", style=['bold'])
    print("Version 0.0")