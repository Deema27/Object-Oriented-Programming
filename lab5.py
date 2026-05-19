# 1 - Import packages and define classes
import pygame, pygwidgets, sys
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hunger = 50
        self.energy = 50

    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(self.name, 'just ate.\n')
        

    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.\n') 

    def play(self, minutes):
        self.energy -= (minutes * 2)
        self.hunger += minutes
        print(f'{self.name} just played for {minutes} minutes.\n') 

    @abstractmethod
    def speak(self):
        pass




class Cat(Animal):
    def __init__(self, name, gender, breed, age):
        super().__init__(name, gender)
        self.breed = breed
        self.age = age
    
    def show(self):
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. '\
              f'{self.name} is {self.age} year(s) old.')        
        print(f'Energy level: {self.energy}.'\
              f' Hunger level: {self.hunger}.\n')

    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Meow!\n')




class Dog(Animal):
    def __init__(self, name, gender, breed, age):
        super().__init__(name, gender)
        self.breed = breed
        self.age = age
    
    def show(self):
        print(f'Dog: {self.name} is a {self.gender} {self.breed}. '\
              f'{self.name} is {self.age} year(s) old.')        
        print(f'Energy level: {self.energy}.'\
              f' Hunger level: {self.hunger}.\n')

    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Ruff!\n')




class Fish(Animal):
    def show(self):
        print(f'Fish: {self.name} is a {self.gender} fish.')        
        print(f'Energy level: {self.energy}.'\
              f' Hunger level: {self.hunger}.\n')

    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Glub!\n')


    

class AnimalShelter():
    def __init__(self):
        self.animalDict = {}
        self.nextId = 0

    def add(self, name, gender, breed=None, age=None, pet_type=None):
        if pet_type == 'cat':
            self.animalDict[self.nextId] = Cat(name, gender, breed, age)
        elif pet_type == 'dog':
            self.animalDict[self.nextId] = Dog(name, gender, breed, age)
        elif pet_type == 'fish':
            self.animalDict[self.nextId] = Fish(name, gender)
            
        self.nextId += 1
        return self.nextId-1
    
    def display(self, aNum):
        self.animalDict[aNum].show()
        
    def display_all(self):
        for animal in self.animalDict.values():
            animal.show()

    def feed_all(self):
        for animal in self.animalDict.values():
            animal.eat()

    def speak_all(self):
        for animal in self.animalDict.values():
            animal.speak()


# main code

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
# None

# 5 - Initialize variables
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


# Manually add the first cat, Garfield, to the shelter
oAnimalShelter = AnimalShelter()
newId = oAnimalShelter.add('Garfield', 'male', 'Tabby', 5, 'cat')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # 8 - Do any "per frame" actions

        name_input.handleEvent(event)
        name = name_input.getValue()

        breed_input.handleEvent(event)
        breed = breed_input.getValue()

        age_input.handleEvent(event)
        age = age_input.getValue()

        cat_button.handleEvent(event)
        cat = cat_button.getValue()

        dog_button.handleEvent(event)
        dog = dog_button.getValue()

        fish_button.handleEvent(event)
        fish = fish_button.getValue()

        female_button.handleEvent(event)
        female = female_button.getValue()

        male_button.handleEvent(event)
        male = male_button.getValue()

        unknown_button.handleEvent(event)
        unknown = unknown_button.getValue()


        if fish:
            pet_type = 'fish'
            breed_title.hide()
            breed_input.hide()
            age_title.hide()
            age_input.hide()
        elif cat:
            pet_type = 'cat'
            breed_title.show()
            breed_input.show()
            age_title.show()
            age_input.show()
        elif dog:
            pet_type = 'dog'
            breed_title.show()
            breed_input.show()
            age_title.show()
            age_input.show()


        if female:
            gender = 'female'
        elif male:
            gender = 'male'
        elif unknown:
            gender = 'unknown'

        if add_button.handleEvent(event):

            if len(name) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Name is required', fontSize=30, textColor=RED)
            elif fish:
                ID = oAnimalShelter.add(name, gender, pet_type='fish')
                status_text = pygwidgets.DisplayText(window, (40, 380), f'Name: {name}   ID: {ID}', fontSize=30, textColor=WHITE)

                name_input.clearText() 
            elif len(breed) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Breed is required', fontSize=30, textColor=RED)
            elif len(age) == 0:
                status_text = pygwidgets.DisplayText(window, (40, 380), 'Age is required', fontSize=30, textColor=RED)
            elif not age.isdigit():
               status_text = pygwidgets.DisplayText(window, (40, 380), 'Age must be an integer', fontSize=30, textColor=RED)           
            else:
                ID = oAnimalShelter.add(name, gender, breed, age, pet_type)
                status_text = pygwidgets.DisplayText(window, (40, 380), f'Name: {name}   ID: {ID}', fontSize=30, textColor=WHITE)
                
                name_input.clearText()
                breed_input.clearText()
                age_input.clearText()
    

        if feed_button.handleEvent(event):

            oAnimalShelter.feed_all()
    

        if speak_button.handleEvent(event):

            oAnimalShelter.speak_all()


        if show_button.handleEvent(event):

            oAnimalShelter.display_all()
        
    
    # 9 - Clear the window
    window.fill(BLUE)
    
    # 10 - Draw all window elements
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
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
