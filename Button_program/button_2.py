''' Description: 
defines a SimpleButton class using a state machine to 
handle mouse interaction, clicks, and optional callback functions '''

# 1 - Import packages
import pygame
from pygame.locals import *

# SimpleButton class handles mouse-driven button behavior using a state machine
class SimpleButton():

    # Button states (idle, pressed, dragged off)
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISARMED = 'disarmed'

    # 2 - Initialize button
    def __init__(self, window, loc, up, down, callBack=None):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)
        self.callBack = callBack

        # Rectangle used for collision detection
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    # 3 - Handle mouse events and update state
    def handleEvent(self, eventObj):

        # Ignore non-mouse events
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        # Button not being interacted with
        if self.state == SimpleButton.STATE_IDLE:
            if eventObj.type == MOUSEBUTTONDOWN and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        # Mouse is pressed on button
        elif self.state == SimpleButton.STATE_ARMED:

            if eventObj.type == MOUSEBUTTONUP and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE

                # Run callback if provided
                if self.callBack is not None:
                    self.callBack()

                return True

            if eventObj.type == MOUSEMOTION and not eventPointInButtonRect:
                self.state = SimpleButton.STATE_DISARMED

        # Mouse dragged off button while pressed
        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    # 4 - Draw button on screen
    def draw(self):

        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        else:
            self.window.blit(self.surfaceUp, self.loc)
