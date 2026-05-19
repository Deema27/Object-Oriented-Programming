class Cat:
    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.energy = 50
        self.hunger = 50
        self.age = age
        
    def show(self):
        return (
            f'Cat: {self.name} is a {self.gender} {self.breed}. {self.name} is {self.age} year(s) old. \n'
            f'Energy level: {self.energy}. Hunger level: {self.hunger}.'
            )
    
    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(f'{self.name} just ate.')

    def meow(self):
        self.energy -= 2
        print(f'{self.name} says: Meow!')

    def play(self, minutes):
        self.energy = self.energy - (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just played for {minutes} minutes.')

    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.')

class AnimalShelter:
    
    def __init__(self):
        self.objectsdict = {}
        self.idnumber = 0

    def add(self, name, gender, breed, age):
        oCat = Cat(name, gender, breed, age)
        newidnumber = self.idnumber
        self.objectsdict[newidnumber] = oCat
        self.idnumber += 1
        return newidnumber

    def display(self, aNum):
        oCat = self.objectsdict[aNum]
        print(oCat.show())


    def display_all(self):
        for AnimalIdNumber in self.objectsdict:
            oCat = self.objectsdict[AnimalIdNumber]
            print('   Account number:', AnimalIdNumber)
            print(oCat.show())



oAnimalShelter = AnimalShelter()
oAnimalShelter.add("Garfield", "male", "Tabby", 5)
while True:
    action = input('\nPress I for info, A to add an account, D to display all, or Q to quit: ')
    if len(action) > 1:
        action = action[0]  # just use first letter
    action = action.upper()  # force uppercase
    
    if action == 'I':
        ID = int(input("What is your cat's ID?"))
        oAnimalShelter.display(ID)
    elif action == 'A':
       name = input("What is the cat's name?")
       age = int(input("What is the cat's age?"))
       breed = input("What is the cat's breed?")
       gender = input("What is the cat's gender?")
       oAnimalShelter.add(name, gender, breed, age)
    elif action == 'D':
        oAnimalShelter.display_all()
    elif action == 'Q':
        break
    
print('Bye')

    



















