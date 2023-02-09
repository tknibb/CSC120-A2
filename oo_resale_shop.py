from computer import *

class ResaleShop:
    name = "Taylor's Store"
    inventory: list

    #constructor
    def __init__(self):
        self.inventory = []

    #buy a new computer and append it to inventory
    def buy(self, computer: Computer):
        self.inventory.append(computer)

    #selling a computer and removing it from inventory 
    def sell(self, computer: Computer):
        if self.inventory == []:
            print("No item in inventory to sell.")
        else:
            self.inventory.remove(computer)
        
    #printing items in inventory
    def print_inventory(self, computer: Computer):
        if self.inventory == []:
            print("No items in inventory.\n")
        else:
            for computer in self.inventory:
                computer.printDetails()