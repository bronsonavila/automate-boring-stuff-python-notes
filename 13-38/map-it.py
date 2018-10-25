#! /usr/bin/env python3

import webbrowser
import sys
import pyperclip

# Check if command line arguments were passed:
if len(sys.argv) > 1:
    # Concatenate arguments to form a valid street address, e.g.,
    # ['mapit.py', '123', 'Main', 'St.'] -> '123 Main St.'
    address = ' '.join(sys.argv[1:])
else:
    # Get address from the user's clipboard if no arguments provided:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
