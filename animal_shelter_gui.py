''' Description:
Creates an animal shelter management system using
OOP concepts and a graphical interface. Users can add
animals (cats, dogs, fish), feed them, and interact with
the shelter through a GUI built with pygame and pygwidgets.'''

# 1 - Import packages and define classes
import pygame, pygwidgets, sys
from abc import ABC, abstractmethod


#Abstract base class representing a general animal
class Animal(ABC):

    #Initialize common animal attributes
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hunger = 50
        self.energy = 50

    #Animal eats and updates stats
    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(self.name, 'just ate.\n')

    #Animal takes a nap and regains energy
    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.\n')

    #Animal plays and loses energy
    def play(self, minutes):
        self.energy -= (minutes * 2)
        self.hunger += minutes
        print(f'{self.name} just played for {minutes} minutes.\n')

    #Abstract method to be implemented by subclasses
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

    #Display cat information
    def show(self):
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. '
              f'{self.name} is {self.age} year(s) old.')
        print(f'Energy level: {self.energy}.'
              f' Hunger level: {self.hunger}.\n')

    #Cat speaks
    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Meow!\n')


#Dog class inherits from Animal
class Dog(Animal):

    #Initialize dog-specific attributes
    def __init__(self, name, gender, breed, age):
        super().__init__(name, gender)
        self.breed = breed
        self.age = age

    #Display dog information
    def show(self):
        print(f'Dog: {self.name} is a {self.gender} {self.breed}. '
              f'{self.name} is {self.age} year(s) old.')
        print(f'Energy level: {self.energy}.'
              f' Hunger level: {self.hunger}.\n')

    #Dog speaks
    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Ruff!\n')


#Fish class inherits from Animal
class Fish(Animal):

    #Display fish information
    def show(self):
        print(f'Fish: {self.name} is a {self.gender} fish.')
        print(f'Energy level: {self.energy}.'
              f' Hunger level: {self.hunger}.\n')

    #Fish speaks
    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Glub!\n')


#Animal shelter class to manage animals
class AnimalShelter():

    #Initialize dictionary and ID counter
    def __init__(self):
        self.animalDict = {}
        self.nextId = 0

    #Add an animal to the shelter
    def add(self, name, gender, breed=None, age=None, pet_type=None):
        if pet_type == 'cat':
            self.animalDict[self.nextId] = Cat(name, gender, breed, age)
        elif pet_type == 'dog':
            self.animalDict[self.nextId] = Dog(name, gender, breed, age)
        elif pet_type == 'fish':
            self.animalDict[self.nextId] = Fish(name, gender)

        self.nextId += 1
        return self.nextId - 1

    #Display a single animal
    def display(self, aNum):
        self.animalDict[aNum].show()

    #Display all animals
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


# main code

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

#Initialize pygame environment
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#Initialize UI elements
title_text = pygwidgets.DisplayText(window, (50, 20), 'Add an Animal to the Shelter', fontSize=40)

type_title = pygwidgets.DisplayText(window, (50, 70), 'Type:', fontSize=30)
cat_button = pygwidgets.TextRadioButton(window, (140, 70), 'Type:', 'Cat', fontSize=25)
dog_button = pygwidgets.TextRadioButton(window, (250, 70), 'Type:', 'Dog', fontSize=25)
fish_button = pygwidgets.TextRadioButton(window, (340, 70), 'Type:', 'Fish', fontSize=25)

name_title = pygwidgets.DisplayText(window, (50, 120), 'Name:', fontSize=30)
name_input = pygwidgets.InputText(window, (120, 120), initialFocus=True, focusColor=RED)

gender_title = pygwidgets.DisplayText(window, (50, 170), 'Gender:', fontSize=30)
female_button = pygwidgets.TextRadioButton(window, (140, 170), 'Gender:', 'Female', fontSize=25)
male_button = pygwidgets.TextRadioButton(window, (250, 170), 'Gender:', 'Male', fontSize=25)
unknown_button = pygwidgets.TextRadioButton(window, (340, 170), 'Gender:', 'Unknown', fontSize=25, value=True)

breed_title = pygwidgets.DisplayText(window, (50, 230), 'Breed:', fontSize=30)
breed_input = pygwidgets.InputText(window, (120, 230), focusColor=RED)

age_title = pygwidgets.DisplayText(window, (50, 280), 'Age:', fontSize=30)
age_input = pygwidgets.InputText(window, (110, 280), focusColor=RED)

status_text = pygwidgets.DisplayText(window, (40, 360), 'All fields are required.', fontSize=30)

add_button = pygwidgets.TextButton(window, (390, 300), 'Add')
feed_button = pygwidgets.TextButton(window, (50, 420), 'Feed All')
speak_button = pygwidgets.TextButton(window, (250, 420), 'Speak to All')
show_button = pygwidgets.TextButton(window, (420, 420), 'Show all cats (in shell)')

#Create shelter and add default animal
oAnimalShelter = AnimalShelter()
newId = oAnimalShelter.add('Garfield', 'male', 'Tabby', 5, 'cat')

#Main loop
while True:

    #Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Handle input fields
        name_input.handleEvent(event)
        breed_input.handleEvent(event)
        age_input.handleEvent(event)

        cat_button.handleEvent(event)
        dog_button.handleEvent(event)
        fish_button.handleEvent(event)

        female_button.handleEvent(event)
        male_button.handleEvent(event)
        unknown_button.handleEvent(event)

        #Determine selected pet type
        if fish_button.getValue():
            pet_type = 'fish'
            breed_title.hide()
            breed_input.hide()
            age_title.hide()
            age_input.hide()

        elif cat_button.getValue():
            pet_type = 'cat'
            breed_title.show()
            breed_input.show()
            age_title.show()
            age_input.show()

        elif dog_button.getValue():
            pet_type = 'dog'
            breed_title.show()
            breed_input.show()
            age_title.show()
            age_input.show()

        #Determine gender
        if female_button.getValue():
            gender = 'female'
        elif male_button.getValue():
            gender = 'male'
        else:
            gender = 'unknown'

        #Add animal
        if add_button.handleEvent(event):

            if len(name_input.getValue()) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Name is required', fontSize=30, textColor=RED)

            elif fish_button.getValue():
                ID = oAnimalShelter.add(name_input.getValue(), gender, pet_type='fish')
                status_text = pygwidgets.DisplayText(window, (40, 380), f'Name: {name_input.getValue()}   ID: {ID}', fontSize=30, textColor=WHITE)

            elif len(breed_input.getValue()) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Breed is required', fontSize=30, textColor=RED)

            elif len(age_input.getValue()) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Age is required', fontSize=30, textColor=RED)

            else:
                ID = oAnimalShelter.add(name_input.getValue(), gender, breed_input.getValue(), age_input.getValue(), pet_type)
                status_text = pygwidgets.DisplayText(window, (40, 380), f'Name: {name_input.getValue()}   ID: {ID}', fontSize=30, textColor=WHITE)

    #Draw UI
    window.fill(BLUE)

    title_text.draw()

    name_title.draw()
    name_input.draw()

    type_title.draw()
    cat_button.draw()
    dog_button.draw()
    fish_button.draw()

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
    feed_button.draw()
    speak_button.draw()
    show_button.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
