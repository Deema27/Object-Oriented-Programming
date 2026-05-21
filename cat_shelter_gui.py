''' Description:
Creates a simple animal shelter management system
focused on adding and displaying cats using OOP and
a pygame graphical interface.'''

# 1 - Import packages and define classes
import pygame, pygwidgets, sys
from abc import ABC, abstractmethod


#Abstract base class for all animals
class Animal(ABC):

    #Initialize common animal attributes
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hunger = 50
        self.energy = 50

    #Increase energy and reduce hunger when eating
    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(self.name, 'just ate.')

    #Increase energy based on nap time and increase hunger
    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.')

    #Decrease energy and increase hunger when playing
    def play(self, minutes):
        self.energy -= (minutes * 2)
        self.hunger += minutes
        print(f'{self.name} just played for {minutes} minutes.')

    #Abstract method to be defined by subclasses
    @abstractmethod
    def speak(self):
        pass


#Cat class inherits from Animal
class Cat(Animal):

    #Initialize cat-specific attributes
    def __init__(self, name, gender, breed, age):
        super().__init__(name, gender)
        self.breed = breed
        self.age = age

    #Display cat details in console
    def show(self):
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. '
              f'{self.name} is {self.age} year(s) old.')
        print(f'Energy level: {self.energy}.'
              f' Hunger level: {self.hunger}.\n')

    #Cat sound behavior
    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Meow!')


#Dog class inherits from Animal (defined but not used in this version)
class Dog(Animal):

    def __init__(self, name, gender, breed, age):
        super().__init__(name, gender)
        self.breed = breed
        self.age = age

    def show(self):
        print(f'Dog: {self.name} is a {self.gender} {self.breed}. '
              f'{self.name} is {self.age} year(s) old.')
        print(f'Energy level: {self.energy}.'
              f' Hunger level: {self.hunger}.\n')

    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Ruff!')


#Fish class inherits from Animal (defined but not fully used in GUI)
class Fish(Animal):

    def show(self):
        print(f'Fish: {self.name} is a {self.gender}. '
              f'{self.name} is {self.age} year(s) old.')
        print(f'Energy level: {self.energy}.'
              f' Hunger level: {self.hunger}.\n')

    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Glub!')


#Animal shelter class manages all animals in the system
class AnimalShelter():

    #Initialize dictionary and ID counter
    def __init__(self):
        self.animalDict = {}
        self.nextId = 0

    #Add a new animal to the shelter
    def add(self, name, gender, breed, age, pet_type):
        if pet_type == 'cat':
            self.animalDict[self.nextId] = Cat(name, gender, breed, age)

        elif pet_type == 'dog':
            self.animalDict[self.nextId] = Dog(name, gender, breed, age)

        elif pet_type == 'fish':
            self.animalDict[self.nextId] = Fish(name, gender)

        self.nextId += 1
        return self.nextId - 1

    #Display one animal by ID
    def display(self, aNum):
        self.animalDict[aNum].show()

    #Display all animals in shelter
    def display_all(self):
        for animal in self.animalDict.values():
            animal.show()

    #Feed all animals
    def feed_all(self):
        for animal in self.animalDict.values():
            animal.eat()

    #Make all animals speak
    def speak_all(self):
        for animal in self.animalDict.values():
            animal.speak()


# ---------------- MAIN PROGRAM ---------------- #

#Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#Set window size and FPS
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

#Initialize pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#Create UI elements
title_text = pygwidgets.DisplayText(window, (50, 50), 'Add a Cat to the Shelter', fontSize=40)

name_title = pygwidgets.DisplayText(window, (50, 100), 'Name:', fontSize=30)
name_input = pygwidgets.InputText(window, (120, 100), initialFocus=True, focusColor=RED)

gender_title = pygwidgets.DisplayText(window, (50, 150), 'Gender:', fontSize=30)
female_button = pygwidgets.TextRadioButton(window, (140, 150), 'Gender:', 'Female', fontSize=25)
male_button = pygwidgets.TextRadioButton(window, (250, 150), 'Gender:', 'Male', fontSize=25)
unknown_button = pygwidgets.TextRadioButton(window, (340, 150), 'Gender:', 'Unknown', fontSize=25, value=True)

breed_title = pygwidgets.DisplayText(window, (50, 200), 'Breed:', fontSize=30)
breed_input = pygwidgets.InputText(window, (120, 200), focusColor=RED)

age_title = pygwidgets.DisplayText(window, (50, 250), 'Age:', fontSize=30)
age_input = pygwidgets.InputText(window, (110, 250), focusColor=RED)

status_text = pygwidgets.DisplayText(window, (40, 380), 'All fields are required.', fontSize=30)

add_button = pygwidgets.TextButton(window, (340, 300), 'Add')

show_button = pygwidgets.TextButton(window, (420, 420), 'Show all cats (in shell)')


#Create shelter and add default cat
oAnimalShelter = AnimalShelter()
newId = oAnimalShelter.add('Garfield', 'male', 'Tabby', 5, 'cat')

#Main loop runs continuously
while True:

    #Handle events
    for event in pygame.event.get():

        #Exit program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Handle user input fields
        name_input.handleEvent(event)
        breed_input.handleEvent(event)
        age_input.handleEvent(event)

        female_button.handleEvent(event)
        male_button.handleEvent(event)
        unknown_button.handleEvent(event)

        #Set gender based on selection
        if female_button.getValue():
            gender = 'female'
        elif male_button.getValue():
            gender = 'male'
        else:
            gender = 'unknown'

        #Add animal when button is clicked
        if add_button.handleEvent(event):

            #Validate inputs
            if len(name_input.getValue()) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Name is required', fontSize=30, textColor=RED)

            elif len(breed_input.getValue()) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Breed is required', fontSize=30, textColor=RED)

            elif len(age_input.getValue()) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Age is required', fontSize=30, textColor=RED)

            elif not age_input.getValue().isdigit():
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Age must be an integer', fontSize=30, textColor=RED)

            else:
                #Add cat to shelter
                ID = oAnimalShelter.add(
                    name_input.getValue(),
                    gender,
                    breed_input.getValue(),
                    age_input.getValue(),
                    'cat'
                )

                #Show success message
                status_text = pygwidgets.DisplayText(
                    window,
                    (40, 380),
                    f'Name: {name_input.getValue()}   ID: {ID}',
                    fontSize=30,
                    textColor=WHITE
                )

                #Clear input fields
                name_input.clearText()
                breed_input.clearText()
                age_input.clearText()

        #Display all animals in console
        if show_button.handleEvent(event):
            oAnimalShelter.display_all()

    #Clear screen
    window.fill(BLUE)

    #Draw UI elements
    title_text.draw()

    name_title.draw()
    name_input.draw()

    gender_title.draw()
    female_button.draw()
    male_button.draw()
    unknown_button.draw()

    breed_title.draw()
    breed_input.draw()

    age_title.draw()
    age_input.draw()

    status_text.draw()

    add_button.draw()
    show_button.draw()

    #Update display
    pygame.display.update()

    #Control frame rate
    clock.tick(FRAMES_PER_SECOND)
