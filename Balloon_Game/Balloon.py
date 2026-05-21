''' Description: 
defines a balloon popping game using an abstract base Balloon class 
and multiple subclasses with different sizes, speeds, and point values '''

# 1 - Import packages
import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from abc import ABC, abstractmethod

# Base Balloon class (abstract)
class Balloon(ABC):

    # Shared pop sound (loaded once for all balloons)
    popSoundLoaded = False
    popSound = None

    # 2 - Initialize base balloon
    @abstractmethod
    def __init__(self, window, maxWidth, maxHeight, ID,
                 oImage, size, nPoints, speedY):

        self.window = window
        self.ID = ID
        self.balloonImage = oImage
        self.size = size
        self.nPoints = nPoints
        self.speedY = speedY

        # Load pop sound only once
        if not Balloon.popSoundLoaded:
            Balloon.popSoundLoaded = True
            Balloon.popSound = pygame.mixer.Sound('sounds/balloonPop.wav')

        # Set balloon dimensions
        balloonRect = self.balloonImage.getRect()
        self.width = balloonRect.width
        self.height = balloonRect.height

        # Random starting position (below screen)
        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)

        self.balloonImage.setLoc((self.x, self.y))

    # 3 - Check if balloon was clicked
    def clickedInside(self, mousePoint):

        myRect = pygame.Rect(self.x, self.y, self.width, self.height)

        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return True, self.nPoints
        else:
            return False, 0

    # 4 - Update balloon movement
    def update(self):

        self.y = self.y - self.speedY
        self.balloonImage.setLoc((self.x, self.y))

        if self.y < -self.height:
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    # 5 - Draw balloon
    def draw(self):
        self.balloonImage.draw()

    # 6 - Cleanup
    def __del__(self):
        print(self.size, 'Balloon', self.ID, 'is going away')


# Small balloon subclass
class BalloonSmall(Balloon):

    balloonImage = pygame.image.load('images/redBalloonSmall.png')

    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonSmall.balloonImage)

        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Small', 30, 3.1)


# Medium balloon subclass
class BalloonMedium(Balloon):

    balloonImage = pygame.image.load('images/redBalloonMedium.png')

    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonMedium.balloonImage)

        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Medium', 20, 2.2)


# Large balloon subclass
class BalloonLarge(Balloon):

    balloonImage = pygame.image.load('images/redBalloonLarge.png')

    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonLarge.balloonImage)

        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Large', 10, 1.5)


# Mega balloon subclass (multi-hit balloon)
class MegaBalloon(Balloon):

    def __init__(self, window, maxWidth, maxHeight, ID):

        self.images = [
            pygame.image.load('images/megaBalloon.png'),
            pygame.image.load('images/megaBalloon1.png'),
            pygame.image.load('images/megaBalloon2.png'),
            pygame.image.load('images/megaBalloon3.png')
        ]

        self.balloonImage = self.images[0]
        self.hitCount = 0

        oImage = pygwidgets.Image(window, (0, 0), self.balloonImage)

        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Mega', 40, 1.5)

    # 7 - Handle clicks with multi-hit behavior
    def clickedInside(self, mousePoint):

        myRect = pygame.Rect(self.x, self.y, self.width, self.height)

        if myRect.collidepoint(mousePoint):

            self.hitCount += 1

            if self.hitCount < len(self.images):
                self.balloonImage = self.images[self.hitCount]
                Balloon.popSound.play()
                return True, 0
            else:
                Balloon.popSound.play()
                return True, self.nPoints
        else:
            return False, 0

    # 8 - Check if balloon is fully popped
    def isReadyToPop(self):
        return self.hitCount >= len(self.images)
