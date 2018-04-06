import curses
import client_file, CLID


#Usually called stdscr, but that isn't readable and "standard_screen" or similar is simply too long for the purpose, I'm not looking to add more that one init anyways
global screen
screen = None

def initcurse():
    #Initializing as described in https://docs.python.org/2/howto/curses.html
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True) #Except here, where they recommend the integer 1 instead of True for some reason. That's wrong, and unreadable.

def killcurse():
    #As initcurse
    curses.nocbreack()
    screen.keypad(False)
    curses.echo
    curses.endwin

async def display_chat(channel):
    #Look at TODO of client_file
