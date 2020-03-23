#! python3

import webbrowser as wb
import sys
import pyperclip

if len(sys.argv) > 1:
    #sys.argv works as a list to store command line inputs
    #get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    address = pyperclip.paste()

wb.open("https://www.google.com/maps/search/" + address)
