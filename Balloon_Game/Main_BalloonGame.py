''' Description: 
Main controller for the Balloon Pop game.
Handles game loop, UI elements (score, status, start button),
and communicates with BalloonMgr to run gameplay. '''

# 1 - Import packages
from pygame.locals import *
import pygwidgets
import sys
import pygame
from BalloonMgr import *

# 2 - Define constants
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets / create UI elements
oScoreDisplay = pygwidgets.DisplayText(
    window,
    (10, USABLE_WINDOW_HEIGHT + 25),
    'Score: 0',
    textColor=BLACK,
    backgroundColor=None,
    width=140,
    fontSize=24
)

oStatusDisplay = pygwidgets.DisplayText(
    window,
    (180, USABLE_WINDOW_HEIGHT + 25),
    '',
    textColor=BLACK,
    backgroundColor=None,
    width=300,
    fontSize=24
)

oStartButton = pygwidgets.TextButton(
    window,
    (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10),
    'Start'
)

# 5 - Initialize game manager and state
oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False  # game starts paused until Start is clicked

# 6 - Game loop
while True:

    # 7 - Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            # Pass input events to balloon manager
            oBalloonMgr.handleEvent(event)

            # Update score display
            theScore = oBalloonMgr.getScore()
            oScoreDisplay.setValue('Score: ' + str(theScore))

        elif oStartButton.handleEvent(event):
            # Start a new game
            oBalloonMgr.start()
            oScoreDisplay.setValue('Score: 0')
            playing = True
            oStartButton.disable()

    # 8 - Update game state each frame
    if playing:
        oBalloonMgr.update()

        nPopped = oBalloonMgr.getCountPopped()
        nMissed = oBalloonMgr.getCountMissed()

        oStatusDisplay.setValue(
            'Popped: ' + str(nPopped) +
            '   Missed: ' + str(nMissed) +
            '   Out of: ' + str(N_BALLOONS)
        )

        # End game when all balloons are accounted for
        if (nPopped + nMissed) == N_BALLOONS:
            playing = False
            oStartButton.enable()

    # 9 - Clear screen
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw everything
    if playing:
        oBalloonMgr.draw()

    pygame.draw.rect(
        window,
        GRAY,
        pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT)
    )

    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()

    # 11 - Update display
    pygame.display.update()

    # 12 - Frame rate control
    clock.tick(FRAMES_PER_SECOND)
