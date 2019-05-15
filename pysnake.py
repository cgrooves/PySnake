#!/usr/bin/env python

import curses
import numpy as np

# Snake class
class Snake:
    
    def __init__(self,numSegments,startX,startY,velocity):
        
        self.numSegments = numSegments

        # Construct the body
        self.body = []
        for i in range(numSegments):
            seg = Segment(np.array([startX-i,startY]),velocity)
            self.body.append(seg)

    def move(self,velocity):

        # for each segment in the body, from last to first:
        for i in range(self.numSegments-1,-1,-1):

            # if this is the head, then the velocity is the function parameter
            if i == self.numSegments-1:
                self.body[i].vel = velocity
            else:
                self.body[i].vel = self.body[i+1].vel

            self.body[i].move()

        return

    def draw(self, win):
        """
        Draw the snake body onto the window
        """
        win.clear()
        # for each segment
        for seg in self.body:
            
            # draw it on the screen
            win.addch(int(seg.pos[1]),int(seg.pos[0]),curses.ACS_CKBOARD)

class Segment:
    """
    Class for defining a snake's body segment. Member variables
    for it's position and velocity.
    """
    
    def __init__(self, pos, vel):
        """
        Pos and vel are numpy arrays.
        """

        self.pos = pos
        self.vel = vel

        return

    def move(self):
        """
        Update the segment's position based on its current
        velocity
        """
        self.pos += self.vel

        return

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
    velocity = np.array([1,0])
    snake = Snake(4,int(sizeX/2),int(sizeY/2),velocity)
    key = curses.KEY_RIGHT

    # Main Loop
    while True:

        # check for updated key input
        new_key = win.getch()
        key = key if new_key == -1 else new_key
        
        # update snake position
        if key == curses.KEY_DOWN:
            velocity = np.array([0,1])
        elif key == curses.KEY_UP:
            velocity = np.array([0,-1])
        elif key == curses.KEY_RIGHT:
            velocity = np.array([1,0])
        elif key == curses.KEY_LEFT:
            velocity = np.array([-1,0])

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
