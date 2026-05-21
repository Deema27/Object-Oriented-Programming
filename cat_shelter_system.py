''' Description: 
creates a simple console-based animal shelter system t
hat stores cats, allows adding cats, and displays cat information using OOP '''

#Class representing a Cat
class Cat:
    
    #Initialize cat attributes
    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.energy = 50
        self.hunger = 50
        self.age = age
        
    #Returns formatted string with cat details
    def show(self):
        return (
            f'Cat: {self.name} is a {self.gender} {self.breed}. {self.name} is {self.age} year(s) old. \n'
            f'Energy level: {self.energy}. Hunger level: {self.hunger}.'
        )
    
    #Increase energy and decrease hunger when eating
    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(f'{self.name} just ate.')

    #Cat sound action
    def meow(self):
        self.energy -= 2
        print(f'{self.name} says: Meow!')

    #Update energy and hunger based on play time
    def play(self, minutes):
        self.energy = self.energy - (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just played for {minutes} minutes.')

    #Update energy and hunger based on nap time
    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.')


#Class that manages the animal shelter system
class AnimalShelter:
    
    #Initialize dictionary and ID counter
    def __init__(self):
        self.objectsdict = {}
        self.idnumber = 0

    #Add a new cat and assign an ID
    def add(self, name, gender, breed, age):
        oCat = Cat(name, gender, breed, age)
        newidnumber = self.idnumber
        self.objectsdict[newidnumber] = oCat
        self.idnumber += 1
        return newidnumber

    #Display one cat by ID
    def display(self, aNum):
        oCat = self.objectsdict[aNum]
        print(oCat.show())

    #Display all cats in the shelter
    def display_all(self):
        for AnimalIdNumber in self.objectsdict:
            oCat = self.objectsdict[AnimalIdNumber]
            print('Account number:', AnimalIdNumber)
            print(oCat.show())


#Create shelter object
oAnimalShelter = AnimalShelter()

#Add default cat
oAnimalShelter.add("Garfield", "male", "Tabby", 5)

#Main program loop
while True:
    
    #Get user input for menu option
    action = input('\nPress I for info, A to add an account, D to display all, or Q to quit: ')
    
    #Allow only first letter input
    if len(action) > 1:
        action = action[0]
    
    #Convert input to uppercase
    action = action.upper()
    
    #Display single cat information
    if action == 'I':
        ID = int(input("What is your cat's ID?"))
        oAnimalShelter.display(ID)
        
    #Add new cat to shelter
    elif action == 'A':
        name = input("What is the cat's name?")
        age = int(input("What is the cat's age?"))
        breed = input("What is the cat's breed?")
        gender = input("What is the cat's gender?")
        oAnimalShelter.add(name, gender, breed, age)
        
    #Display all cats
    elif action == 'D':
        oAnimalShelter.display_all()
        
    #Exit program
    elif action == 'Q':
        break

#Exit message
print('Bye')
