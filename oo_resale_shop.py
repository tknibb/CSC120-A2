from computer import *

class ResaleShop:
    name = "Taylor's Store"
    inventory: list

    def __init__(self):
        self.inventory = []

    def buy(self, computer: Computer):
        self.inventory.append(computer)

    def sell(self, computer: Computer):
        self.inventory.remove(computer)
        
    def print_inventory(self, computer: Computer):
        for computer in self.inventory:
            computer.printDetails()

   
        