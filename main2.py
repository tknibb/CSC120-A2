from oo_resale_shop import ResaleShop
from computer import Computer


def main():
        comp = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500, 1)
        resale = ResaleShop()

        # Print a little banner
        print("-" * 21)
        print(resale.name)
        print("-" * 21)

        # Add it to the resale store's inventory
        print("Buying", comp.description)
        print("Adding to inventory...")
        resale.buy(comp)
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        resale.print_inventory(comp)
        print("Done.\n")

        # Now, let's refurbish it
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID: 1, updating OS to MacOS Monterey")
        comp.updateOS(new_OS)
        print("Updating inventory...")
        comp.refurbish()
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        resale.print_inventory(comp)
        print("Done.\n")
        
        # Now, let's sell it!
        print("Selling Item ID: 1")
        resale.sell(comp)
        print("Done.\n")
        
        # Make sure it worked by checking inventory
        print("Checking inventory...")
        resale.print_inventory(comp)
        print("Done.\n")


if __name__ == "__main__": main()