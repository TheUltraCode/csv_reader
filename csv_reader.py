"""
Copyright (c) 2025 Kyle Nied

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import csv, keyboard, pyperclip

results_data = list()
results_data_index = 0

def copier():
    global results_data, results_data_index
    pyperclip.copy(results_data[results_data_index])
    results_data_index += 1
    if results_data_index == len(results_data):
        results_data_index = 0

print('\nCSV Reader\n')
while True:
    input_var = int(input('Menu:\n(1) Read data from "data.csv".\n(2) Exit program.\n\n>'))
    if input_var == 1:
        with open('data.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            results_data = list(reader)[0]
        key_binding = keyboard.add_hotkey('ctrl + shift', copier)
        print('\nPress (esc) on your keyboard to go back to the main menu.\n',flush=True)
        keyboard.wait('esc')
        keyboard.remove_hotkey(key_binding)
        results_data_index = 0
    elif input_var == 2:
        keyboard.unhook_all()
        break
    else:
        print('\nNot valid input. Try again.\n')
