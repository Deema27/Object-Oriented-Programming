''' Description: 
Simple text display class for rendering static text
onto a pygame window using a font surface. '''

import pygame
from pygame.locals import *

class SimpleText():
    
    def __init__(self, window, loc, value, textColor):
        # Initialize font system (safe even if called multiple times)
        pygame.font.init()

        # Store window and position
        self.window = window
        self.loc = loc

        # Set up font (default font, size 30)
        self.font = pygame.font.SysFont(None, 30)

        # Store text color
        self.textColor = textColor

        # Placeholder so first setValue always triggers rendering
        self.text = None

        # Set initial text
        self.setValue(value)

    def setValue(self, newText):
        # Only re-render text if it has changed (performance optimization)
        if self.text == newText:
            return

        # Update stored text
        self.text = newText

        # Render text into a surface (image) for drawing
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
        # Draw text onto the window at the specified location
        self.window.blit(self.textSurface, self.loc)
