import curses
import pyfiglet
from termcolor import colored
import re
import os

class Termy:
    @staticmethod
    def head_text(text, font="slant", color="white", on_color=None, style=None):
        """Renders the given text in a specified font and color using pyfiglet and termcolor."""
        try:
            figlet = pyfiglet.Figlet(font=font)
            ascii_art = figlet.renderText(text)
            colored_art = colored(ascii_art, color=color, on_color=on_color, attrs=style)
            print(colored_art)
        except Exception as e:
            print(f"Error rendering head_text: {e}")

    @staticmethod
    def p(text, color="white", on_color=None, style=None):
        """Prints the given text in a specified color and style using termcolor."""
        try:
            colored_text = colored(text, color=color, on_color=on_color, attrs=style)
            print(colored_text)
        except Exception as e:
            print(f"Error rendering text: {e}")

    @staticmethod
    def link(url, link_text, color="blue", on_color=None, style=None):
        """Prints a hyperlink with the specified display text and URL."""
        try:
            colored_link_text = colored(link_text, color=color, on_color=on_color, attrs=style)
            print(f"\033]8;;{url}\033\\{colored_link_text}\033]8;;\033\\")
        except Exception as e:
            print(f"Error rendering link: {e}")

    @staticmethod
    def __render_markdown(text):
        """Renders markdown text with appropriate styles and colors."""
        try:
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
        except Exception as e:
            print(f"Error rendering markdown: {e}")
            return text

    @staticmethod
    def use_file(file_path, box_color="white"):
        """Reads a file, renders its markdown content, and prints it inside a box."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                # Render markdown
                rendered_content = Termy.__render_markdown(content)
                # Print content in a box with specified color
                Termy.print_box(rendered_content, box_color)
        except Exception as e:
            print(f"Error reading file: {e}")

    @staticmethod
    def print_box(content, box_color):
        """Prints the given content inside a box with a specified color."""
        try:
            lines = content.split('\n')
            max_length = max(len(line) for line in lines)
            print(f'╔{colored("═" * (max_length + 2), color=box_color)}╗')
            for line in lines:
                print(f'║ {line.ljust(max_length)} ║')
            print(f'╚{colored("═" * (max_length + 2), color=box_color)}╝')
        except Exception as e:
            print(f"Error printing box: {e}")

    @staticmethod
    def btn(text, options, color=None):
        """Creates a menu with clickable buttons using curses."""
        def character(stdscr):
            curses.mousemask(1)

            attributes = {}
            color_map = {
                1: 'red',
                2: 'green',
                3: 'yellow',
                4: 'blue',
                5: 'magenta',
                6: 'cyan',
                7: 'white'
            }
            reverse_color_map = {v: k for k, v in color_map.items()}

            black_bg = curses.COLOR_BLACK
            curses.init_pair(1, 7, black_bg)
            attributes['normal'] = curses.color_pair(1)

            # Initialize highlighted attribute
            curses.init_pair(2, reverse_color_map['white'], black_bg)  # Initialize with white color
            attributes['highlighted'] = curses.color_pair(2)

            # Determine the maximum length of the options
            max_option_length = max(len(label) for label, _ in options)
            box_width = max_option_length + 4  # Adding padding

            option = 0
            while True:
                stdscr.erase()

                # Calculate box dimensions
                start_x = (curses.COLS - box_width) // 2
                start_y = (curses.LINES - len(options) * 3) // 2

                # Draw the text
                stdscr.addstr(start_y - 2, start_x, text, curses.color_pair(1))

                # Draw each option in its own box
                for i, (label, func) in enumerate(options):
                    option_y = start_y + i * 3

                    # Draw the box
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(option_y, start_x, '╔' + '═' * (box_width - 2) + '╗')
                    stdscr.addstr(option_y + 1, start_x, '║' + ' ' * (box_width - 2) + '║')
                    stdscr.addstr(option_y + 2, start_x, '╚' + '═' * (box_width - 2) + '╝')
                    stdscr.attroff(curses.color_pair(1))

                    # Draw the option text
                    if i == option:
                        attr = attributes['highlighted']
                    else:
                        attr = attributes['normal']
                    stdscr.addstr(option_y + 1, start_x + 2, label, attr)

                stdscr.refresh()

                c = stdscr.getch()

                # Handle the arrow keys
                if c == curses.KEY_UP and option > 0:
                    option -= 1
                elif c == curses.KEY_DOWN and option < len(options) - 1:
                    option += 1
                elif c == curses.KEY_MOUSE:
                    _, mx, my, _, _ = curses.getmouse()
                    if start_y <= my < start_y + len(options) * 3:
                        option = (my - start_y) // 3
                        break
                    elif my >= start_y + len(options) * 3:
                        break

            # Call the selected function
            label, func = options[option]
            func()

        try:
            curses.wrapper(character)
        except Exception as e:
            print(f"Error in button menu: {e}")
            
    @staticmethod
    def styled_input(prompt, color="white", on_color=None, style=None, border_color="grey"):
        """Prompts the user for input with a styled prompt message and lines above and below."""
        try:
            # Get terminal width
            terminal_width = os.get_terminal_size().columns // 2

            # Create the styled prompt
            styled_prompt = colored(prompt, color=color, on_color=on_color, attrs=style)

            # Print top border
            print(colored("-" * terminal_width, color=border_color))

            # Print the prompt
            print(styled_prompt, end="")  # Add 'end=""' to avoid adding a newline

            # Get user input
            user_input = input()

            # Print bottom border
            print(colored("-" * terminal_width, color=border_color))

            return user_input
        except Exception as e:
            print(f"Error in styled_input: {e}")
            return input(prompt)
        
if __name__ == "__main__":
    Termy.head_text('Termy', color="blue", style=['bold'])
    print("Version 0.0")

    Termy.p("Termy's usage\n", color="red", style=["bold"])

    Termy.p("Colors - \n", color="white", style=["bold"])

    Termy.p("Grey", color="grey")
    Termy.p("Red", color="red")
    Termy.p("Green", color="green")
    Termy.p("Yellow", color="yellow")
    Termy.p("Blue", color="blue")
    Termy.p("Magenta", color="magenta")
    Termy.p("Cyan", color="cyan")
    Termy.p("White", color="white")


