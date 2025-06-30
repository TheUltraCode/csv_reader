# csv_reader

Small script I have written to help with repetitive data entry tasks. It reads a the first line from a csv file, adds all of the elements from that line to a `list` data-structure, and then allows you to cycle through that list, copying the current element to your clipboard, until you quit the program. The csv file it looks for in the same directory as the script itself is `data.csv` and the key binding for cycling through the list is "ctrl" + "shift".

Relies on two external, third-party modules to function - `keyboard` and `pyperclip`. More information regarding those modules can be found here:
- [https://github.com/boppreh/keyboard](https://github.com/boppreh/keyboard)
- [https://github.com/asweigart/pyperclip](https://github.com/asweigart/pyperclip)

Enjoy. :)
