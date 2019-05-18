#!/usr/bin/env python

import numpy as np
from copy import deepcopy

# Snake class
class Snake:
    
    def __init__(self,numSegments,startX,startY):
        """
        Creates a snake body with numSegments, with head at
        startX and startY. The tail is strung out along the
        x-axis behind the head.
        """
        
        self.numSegments = numSegments

        # Construct the body
        self.body = []

        for i in range(numSegments):
            self.body.append([startX-i, startY])

    def move(self,velocity):
        """
        Moves the snake head by velocity, and makes each piece of
        the tail/body follow the preceding piece.
        """

        # make a copy of the body
        old_body = deepcopy(self.body)

        # move the head
        self.body[0][0] += velocity[0]
        self.body[0][1] += velocity[1]

        # for the rest of the body
        for i in range(1,len(self.body)):
            # move a piece to the next piece's position
            self.body[i] = old_body[i-1]

        return

    def grow(self):
        """
        Adds a piece to the tail.
        """
        
        self.body.append(self.body[-1])

# test
if __name__ == "__main__":

    # test a snake
    s = Snake(3,50,80)
    print(s.body)

    s.move([0,1])
    print(s.body)
    s.move([0,1])
    print(s.body)
    s.move([0,1])
    print(s.body)
