''' Description: 
Manages a collection of balloon objects in the balloon popping game.
Handles creation, updating movement, collision detection (clicks),
scoring, and removal of balloons when popped or missed. '''

import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from Balloon import *

# BalloonMgr class controls all balloons in the game
class BalloonMgr():
    def __init__(self, window, maxWidth, maxHeight):
        # Store window and boundaries for balloon movement/placement
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    def start(self):
        # Reset game state and create a new set of balloons
        self.balloonList = []
        self.nPopped = 0
        self.nMissed = 0
        self.score = 0

        # Create a random mix of balloon types
        for balloonNum in range(0, N_BALLOONS):
            randomBalloonClass = random.choice(
                (BalloonSmall, BalloonMedium, BalloonLarge, MegaBalloon)
            )
            oBalloon = randomBalloonClass(
                self.window,
                self.maxWidth,
                self.maxHeight,
                balloonNum
            )
            self.balloonList.append(oBalloon)

    def handleEvent(self, event):
        # Handle mouse clicks on balloons
        if event.type == MOUSEBUTTONDOWN:

            # Check top-most balloons first (reverse order)
            for oBalloon in reversed(self.balloonList):
                wasHit, nPoints = oBalloon.clickedInside(event.pos)

                if wasHit:
                    # Handle scoring and removal logic
                    if nPoints > 0:

                        # Special handling for Mega balloons
                        if oBalloon.size == 'Mega':
                            if oBalloon.isReadyToPop():
                                self.balloonList.remove(oBalloon)
                                self.nPopped += 1
                                self.score += nPoints
                        else:
                            self.balloonList.remove(oBalloon)
                            self.nPopped += 1
                            self.score += nPoints

                    return  # stop after first hit

    def update(self):
        # Move balloons and remove any that leave the screen
        for oBalloon in self.balloonList:
            status = oBalloon.update()

            if status == BALLOON_MISSED:
                self.balloonList.remove(oBalloon)
                self.nMissed += 1

    def getScore(self):
        # Return current score
        return self.score

    def getCountPopped(self):
        # Return number of balloons popped
        return self.nPopped

    def getCountMissed(self):
        # Return number of balloons missed
        return self.nMissed

    def draw(self):
        # Draw all balloons on the screen
        for oBalloon in self.balloonList:
            oBalloon.draw()
