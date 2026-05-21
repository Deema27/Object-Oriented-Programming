''' Description:
Manages a bakery inventory system that allows
users to add cakes, purchase slices, view cake
information, and compare cake values.'''

class Bakery:

    #Constructor initializes an empty cake list
    def __init__(self):
        self.cakelist = []

    #Adds a new cake object to the bakery
    def add(self, kind, price, slices):
        oCake = Cake(kind, price, slices)
        self.cakelist.append(oCake)

    #Displays information for all cakes
    def display(self):
        for cake in self.cakelist:
            print(cake.describe())

    #Searches for a cake by flavor
    def get_cake(self, kind):
        for cake in self.cakelist:
            if cake.kind == kind:
                return cake
        return None

    #Returns the number of remaining slices for a cake
    def get_remaining_slices(self, flavor):
        cake = self.get_cake(flavor)
        if cake:
            return cake.remaining
        else:
            return None

    #Sells one slice of a cake
    def sell_slice(self, flavor):
        cake = self.get_cake(flavor)

        #Check if cake exists
        if cake:

            #Check if slices remain
            if cake.remaining > 0:
                cake.sell(1)

                #Return price per slice
                return cake.price / cake.slices
            else:
                return None
        else:
            return None


class Cake:

    #Constructor initializes cake information
    def __init__(self, kind, price, slices):
        self.kind = kind
        self.price = price
        self.slices = slices
        self.remaining = slices

    #Returns a description of the cake
    def describe(self):
        return f"The {self.kind} cake costs ${self.price} and is divided into {self.slices} slices."

    #Sells a specified number of slices
    def sell(self, count):

        #Prevent invalid slice amounts
        if count <= 0:
            print("Cannot sell zero or negative slices!")

        #Prevent selling more slices than available
        elif count > self.slices:
            print(f"Cannot sell more slices than we have ({self.slices})!")

        #Subtract sold slices from remaining amount
        else:
            self.remaining -= count
            print(f"This cake has {self.remaining} slices remaining.")

    #Calculates current value of remaining cake
    def get_value(self):
        return (self.price / self.slices) * self.remaining

    #Checks if cake values are equal
    def isEqualTo(self, otherCake):
        return (self.get_value() == otherCake.get_value())

    #Checks if current cake value is less than another cake
    def isLessThan(self, otherCake):
        return (self.get_value() < otherCake.get_value())

    #Checks if current cake value is greater than another cake
    def isGreaterThan(self, otherCake):
        return (self.get_value() > otherCake.get_value())


#Create sample cake objects
spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)

#Sell slices and compare cakes
print(spice_cake.sell(1))
print(chocolate_cake.sell(3))
print(spice_cake.isEqualTo(chocolate_cake))
print(spice_cake.isGreaterThan(chocolate_cake))
print(spice_cake.isLessThan(chocolate_cake))


#Create bakery object
oBakery = Bakery()

#Add starting cakes to bakery
oBakery.add("vanilla", 18, 6)
oBakery.add("coconut", 20, 10)

#Main menu loop
while True:

    #Display menu options
    action = input('\nPress A to add a cake,'\
                   ' I for info about a cake remaining slices,'\
                   ' P for purchasing a slice of a cake,'\
                   ' D for info about all cakes,'\
                   ' or Q to quit: ')

    #Only use first character of input
    if len(action) > 1:
        action = action[0]

    #Convert input to uppercase
    action = action.upper()

    #Add a new cake
    if action == 'A':
        f = input("New cake: what is the flavor? ")
        p = int(input("What is the price for the whole cake?"))
        s = int(input("How many slices are in the cake?"))

        oBakery.add(f, p, s)
        print("Cake added.")

    #Display remaining slices of a cake
    elif action == 'I':
        f = input("Cake info: what flavor? ")

        numSlices = oBakery.get_remaining_slices(f)

        if numSlices:
            print(f"The {f} cake has {numSlices} slices remaining.")
        else:
            print("Cake not found.")

    #Purchase a slice of cake
    elif action == 'P':
        f = input("Buy slice: what flavor? ")

        price = oBakery.sell_slice(f)

        if price:
            print(f"A slice of the {f} cake costs ${price}.")
        else:
            print(f"There are no slices of the {f} cake.")

    #Display all cakes
    elif action == 'D':
        oBakery.display()

    #Quit the program
    elif action == 'Q':
        break
