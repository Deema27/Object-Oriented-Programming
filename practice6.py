


class Bakery:
    
    def __init__(self):
        self.cakelist = []

    def add(self, kind, price, slices):
        oCake = Cake(kind, price, slices)
        self.cakelist.append(oCake)

    def display(self):
        for cake in self.cakelist:
            print(cake.describe())

    def get_cake(self, kind):
        for cake in self.cakelist:
            if cake.kind == kind:
                return cake
        return None

    def get_remaining_slices(self, flavor):
        cake = self.get_cake(flavor)
        if cake:
            return cake.remaining
        else:
            return None

    def sell_slice(self, flavor):
        cake = self.get_cake(flavor)
        if cake:
            if cake.remaining > 0:
                cake.sell(1)
                return cake.price / cake.slices
            else:
                return None
        else:
            return None

class Cake:
    
    def __init__(self, kind, price, slices):
        self.kind = kind
        self.price = price
        self.slices = slices
        self.remaining = slices
    
    def describe(self):
        return f"The {self.kind} cake costs ${self.price} and is divided into {self.slices} slices."

    def sell(self, count):
        if count <= 0:
            print("Cannot sell zero or negative slices!")
        elif count > self.slices:
            print(f"Cannot sell more slices than we have ({self.slices})!")
        else:
            self.remaining -= count
            print(f"This cake has {self.remaining} slices remaining.")

    def get_value(self):
        return (self.price / self.slices) * self.remaining

    def isEqualTo(self, otherCake):
        return (self.get_value() == otherCake.get_value())

    def isLessThan(self, otherCake):
        return (self.get_value() < otherCake.get_value())

    def isGreaterThan(self, otherCake):
        return (self.get_value() > otherCake.get_value())

spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)


print(spice_cake.sell(1))
print(chocolate_cake.sell(3))
print(spice_cake.isEqualTo(chocolate_cake))
print(spice_cake.isGreaterThan(chocolate_cake))
print(spice_cake.isLessThan(chocolate_cake))





oBakery = Bakery()
oBakery.add("vanilla", 18, 6)
oBakery.add("coconut", 20, 10)
while True:
    action = input('\nPress A to add a cake,'\
                   ' I for info about a cake remaining slices,'\
                   ' P for purchasing a slice of a cake,'\
                   ' D for info about all cakes,'\
                   ' or Q to quit: ')
    if len(action) > 1:
        action = action[0] # just use first letter
    action = action.upper() # force uppercase
    if action == 'A':
        f = input("New cake: what is the flavor? ")
        p = int(input("What is the price for the whole cake?"))
        s = int(input("How many slices are in the cake?"))
        oBakery.add(f, p, s)
        print("Cake added.")
    elif action == 'I':
        f = input("Cake info: what flavor? ")
        numSlices = oBakery.get_remaining_slices(f)
        if numSlices:
            print(f"The {f} cake has {numSlices} slices remaining.")
        else:
            print("Cake not found.")
    elif action == 'P':
        f = input("Buy slice: what flavor? ")
        price = oBakery.sell_slice(f)
        if price:
            print(f"A slice of the {f} cake costs ${price}.")
        else:
            print(f"There are no slices of the {f} cake.")
    elif action == 'D':
        oBakery.display()
    elif action == 'Q':
        break
