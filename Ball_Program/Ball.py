''' Description: 
Represents a moving ball that bounces off the window edges '''

import pygame
from pygame.locals import *
import random

# Ball class
class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # store window reference for drawing
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        # load ball image
        self.image = pygame.image.load('images/ball.png')

        # get image dimensions using rect
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height

        # calculate boundaries so ball stays inside window
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        # pick a random starting position within bounds
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # choose random speed in both directions (excluding zero)
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4] 
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # reverse direction if ball hits left or right boundary
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        # reverse direction if ball hits top or bottom boundary
        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # update position using current speed
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        # draw ball at its current position
        self.window.blit(self.image, (self.x, self.y))
