''' Description: 
defines a SimpleButton class using a state machine 
to handle mouse interaction and button clicks in pygame '''

# 1 - Import packages
import pygame
from pygame.locals import *

# SimpleButton class using a state machine for interaction
class SimpleButton():

    # Button states
    STATE_IDLE = 'idle'          # button is not pressed
    STATE_ARMED = 'armed'        # button is pressed and mouse is over it
    STATE_DISARMED = 'disarmed'  # button was pressed but mouse moved off

    # 2 - Initialize button
    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        # Rectangle used for mouse collision detection
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    # 3 - Handle mouse events and update button state
    def handleEvent(self, eventObj):

        # Only respond to mouse events
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        # Idle state (not pressed)
        if self.state == SimpleButton.STATE_IDLE:
            if eventObj.type == MOUSEBUTTONDOWN and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        # Pressed state
        elif self.state == SimpleButton.STATE_ARMED:
            if eventObj.type == MOUSEBUTTONUP and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True

            if eventObj.type == MOUSEMOTION and not eventPointInButtonRect:
                self.state = SimpleButton.STATE_DISARMED

        # Dragged off state
        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    # 4 - Draw button
    def draw(self):

        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        else:
            self.window.blit(self.surfaceUp, self.loc)
