''' Description: 
creates a pygame program where multiple cat images can be 
added, removed, moved with arrow keys, and repositioned by 
clicking, using buttons and collision detection '''

# 1 - Import packages
import pygame, sys, random, pygwidgets

#CatImage class handles individual cat objects
class CatImage():
    
    #Initialize cat image and position
    def __init__(self, window):
        self.window = window
        self.image = pygame.image.load('cat.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.maxX = window.width - self.width
        self.maxY = window.height - self.height
        
        #Set random starting position
        self.new_position()
        
    #Move cat to random location
    def new_position(self):
        self.x = random.randrange(0, self.maxX)
        self.y = random.randrange(0, self.maxY)

    #Return rectangle for collision detection
    def get_rect(self):
        return self.rect

    #Draw cat on screen
    def draw(self):
        self.rect = self.window.blit(self.image, (self.x, self.y))


# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_TO_MOVE = 10

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets
bounceSound = pygame.mixer.Sound('boing.wav')

# 5 - Initialize variables
#Create first cat and list to store all cats
oCat = CatImage(window)
catList = []
catList.append(oCat)

#Create UI buttons
add_cat = pygwidgets.TextButton(window, (150, 400), 'Add cat', textColor=GREEN)
remove_cat = pygwidgets.TextButton(window, (390, 400), 'Remove Cat', textColor=RED)

# 6 - Main loop
while True:

    # 7 - Handle events
    for event in pygame.event.get():

        #Exit program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Add new cat button
        if add_cat.handleEvent(event):
            newCat = CatImage(window)
            catList.append(newCat)

            if len(catList) == 1:
                remove_cat.enable()

        #Remove cat button
        if remove_cat.handleEvent(event):
            if len(catList) > 0:
                catList.pop()

            if len(catList) == 0:
                remove_cat.disable()
                bounceSound.play()

        #Mouse click interaction
        if event.type == pygame.MOUSEBUTTONDOWN:
            for cat in catList:
                if cat.get_rect().collidepoint(event.pos):
                    cat.new_position()

    # 8 - Per frame actions (keyboard movement)
    keyPressedTuple = pygame.key.get_pressed()

    #Get last cat in list (the one being controlled)
    if len(catList) > 0:
        lastCat = catList[-1]
    else:
        lastCat = None

    #Move only last cat using arrow keys
    if lastCat:

        if keyPressedTuple[pygame.K_LEFT]:
            lastCat.x -= N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_RIGHT]:
            lastCat.x += N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_UP]:
            lastCat.y -= N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_DOWN]:
            lastCat.y += N_PIXELS_TO_MOVE

        #Boundary checks with bounce sound
        if lastCat.x < 0:
            lastCat.x = 0
            bounceSound.play()

        if lastCat.x >= lastCat.maxX:
            lastCat.x = lastCat.maxX
            bounceSound.play()

        if lastCat.y < 0:
            lastCat.y = 0
            bounceSound.play()

        if lastCat.y >= lastCat.maxY:
            lastCat.y = lastCat.maxY
            bounceSound.play()

    # 9 - Clear screen
    window.fill(WHITE)

    # 10 - Draw cats and buttons
    for oCat in catList:
        oCat.draw()

    add_cat.draw()
    remove_cat.draw()

    # 11 - Update display
    pygame.display.update()

    # 12 - Frame rate control
    clock.tick(FRAMES_PER_SECOND)
