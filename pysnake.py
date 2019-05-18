#!/usr/bin/env python

import curses
import numpy as np
import snake as Snake
import random

def checkCollisions(snake, xmax, ymax):
    """
    Checks collisions with window walls and within the snake body.
    """

    # Check walls
    for piece in snake.body:
        if piece[0] >= xmax or \
            piece[1] >= ymax or \
            piece[0] < 1 or \
            piece[1] < 1:
            return True

    # check internal collisions
    return internalCollision(snake.body)

def internalCollision(body):
    """
    Looks for duplicates in the param body.
    Returns True if any duplicate is found.
    """

    final_list = []

    for i in body:
        if i not in final_list:
            final_list.append(i)

    if len(final_list) == len(body):
        return False
    else:
        return True
        

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
    snake = Snake.Snake(10,int(sizeX/2),int(sizeY/2))
    key = curses.KEY_RIGHT
    velocity = [1,0]
    keep_playing = True
    food = [int(sizeX*.75),int(sizeY/2)]

    # Main Loop
    while keep_playing:

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

        # Check collisions
        collision = checkCollisions(snake, sizeX, sizeY)

        # Check for end-game conditions
        keep_playing = not collision

        # Check for eating of food
        if snake.body[0] == food:
            snake.grow()
            
            while food in snake.body:
                food = [
                        random.randint(1, sizeX-1),
                        random.randint(1, sizeY-1),
                       ]

        ## Rendering
        # Draw snake
        if keep_playing:
            win.clear()

            for piece in snake.body:
                win.addch(piece[1],piece[0],curses.ACS_CKBOARD)
        
        # Draw food
        win.addch(food[1],food[0],curses.ACS_PI)

    # end main loop
        
    # exit application
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("GAME OVER")
    quit()

# Command-line invocation
if __name__ == "__main__":

    curses.wrapper(snakeLoop())
