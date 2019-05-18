#!/usr/bin/env python

import curses
import numpy as np
import snake

# main loop
def snakeLoop():

    # Curses setup
    stdscr = curses.initscr() # get screen
    curses.curs_set(False)
    # get screen boundaries
    sizeY, sizeX = stdscr.getmaxyx()
    win = curses.newwin(sizeY, sizeX, 0, 0)

    curses.noecho() # no echoing of keys to screen
    curses.cbreak() # no return needed for key input
    
    win.keypad(True)
    win.timeout(100)

    # Initialize game
    velocity = [1,0]
    snake = Snake(4,int(sizeX/2),int(sizeY/2))
    key = curses.KEY_RIGHT

    # Main Loop
    while True:

        # check for updated key input
        new_key = win.getch()
        key = key if new_key == -1 else new_key
        
        # update snake position
        if key == curses.KEY_DOWN:
            velocity = [0,1]
        elif key == curses.KEY_UP:
            velocity = [0,-1]
        elif key == curses.KEY_RIGHT:
            velocity = [1,0]
        elif key == curses.KEY_LEFT:
            velocity = [-1,0]

        snake.move(velocity)

        # draw snake
        snake.draw(win)

    # end main loop
        
    # exit application
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    quit()

# Command-line invocation
if __name__ == "__main__":

    curses.wrapper(snakeLoop())
