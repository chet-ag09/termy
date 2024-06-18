# TermyUI

### Termy is for creating a simple and attractive UI for the terminal, ranging from clickable links to simple buttons, termy has it all!

[Visit PyPI page](https://pypi.org/project/termyUI/)

This is a big project for me hence, I need help maintaining it, if you are interested, shoot an email at - agchetna4@gmail.com

a simple demo with TermyUI.

First, you need to install Termy, for that run the following command - 

```pip install termyUI``
```
from termy import *
import os
import webbrowser

ter = Termy()

def option_1():
  webbrowser.open(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  

def option_2():
    ter.head_text("TermyUI", color="red", style=["bold"])
    ter.p("Write 'python -m termy' in the terminal for all the functions and commands for using termy!", color="blue", style=["bold"])

options = [
    ("Option 1", option_1),
    ("Option 2", option_2),
]
choice = ter.btn("Select an option:", options)

```
