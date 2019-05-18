#!/usr/bin/env python

import curses
import numpy as np
import snake as Snake

# main loop
def snakeLoop():

    ## Environment setup
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

    ## Initialize game
    snake = Snake.Snake(4,int(sizeX/2),int(sizeY/2))
    key = curses.KEY_RIGHT
    velocity = [1,0]

    # Main Loop
    while True:

        ## Update events
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

        ## Game logic
        snake.move(velocity)

        ## Rendering
        # Draw snake
        win.clear()

        for piece in snake.body:
            win.addch(piece[1],piece[0],curses.ACS_CKBOARD)

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
