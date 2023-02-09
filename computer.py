class Computer:

    # Computer attributes 
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    # constructor
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    #print the computer details
    def printDetails(self):
        print("Description: ", self.description)
        print("Processor type: ", self.processor_type)
        print("Hard Drive Capacity: ", self.hard_drive_capacity)
        print("Memory: ", self.memory)
        print("Operating system: ", self.operating_system)
        print("Year made: ", self.year_made)
        print("Price: ", self.price)
        
    #refurbishing the price depending on the year made 
    def refurbish(self):
        if self.year_made < 2000:
            self.price = 0 
        elif self.year_made < 2012:
            self.price = 250 
        elif self.year_made < 2018:
            self.price = 550 
        else:
            self.price = 1000 

    #updating the operating system
    def updateOS(self, new_os: str):
        self.operating_system = new_os
    