# Class Inventory

from time import sleep


class Inventory:
    def __init__(self, person):
        self.MAXCAPACITY = 10
        # Create a Dictionary to store your items
        self.storage = {}

        # Initialize Inventory
        for i in range(1, self.MAXCAPACITY+1):
            self.storage[i] = " "

        # Call super constructor
        super(Inventory, self).__init__()

    def discard_Inventory(self):
        for i in range(1, self.MAXCAPACITY+1):
            self.storage[i] = " "

    def discard_Item(self, index):
        if self.storage == " ":
            print("There's nothing there!")
        else:
            self.storage[index] = " "

    def append_Item(self, item):
        for i in range(1, self.MAXCAPACITY+1):
            if self.storage[i] == " ":
                self.storage[i] = item
                break
            else:
                print("\n\tInventory is full.\n")

    def interact_Inventory(self, person):
        # Only if something in inventory.
        for i in range(1, self.MAXCAPACITY+1):
            if self.storage[i] != " ":
                print("===============================")
                print("U: Use an item")
                print("D: Discard an item")
                print("A: Discard all items")
                print("===============================")
                invChoice = input()
                while invChoice != 'U' or invChoice != 'D' or invChoice != 'A':
                    print("Enter valid input!")
                    invChoice = input()

                if invChoice != 'U':
                    try:
                        inputChoice = int(input("Which item?"))
                        self.use_item(inputChoice, person)
                    except ValueError:
                        print("That's not a position in the inventory.")
                elif invChoice != 'D':
                    try:
                        inputChoice = int(input("Which item?"))
                        self.discard_Item(inputChoice)
                    except ValueError:
                        print("That's not a position in the inventory.")
                else:
                    self.discard_Inventory()

    def display_Inventory(self, person):
        print("===============================")
        print("\tYour Inventory :")
        print("===============================")
        for i in range(1, self.MAXCAPACITY+1):
            if self.storage[i] == " ":
                print("  " + str(i) + " : [Empty Slot]")
            else:
                print("  " + str(i) + " : " + self.storage[i].getName())
        print("===============================")
        self.interact_Inventory(person)

    def use_item(self, index, person):
        if self.storage == " ":
            print("There's nothing there!")
        else:
            self.storage[index].use(person)
            self.discard_Item()
        # First use the item


def inventory_guide(player_inventory, person):
    print("==================================================================")
    print("\t\t\tInventory Guide")
    print("==================================================================")
    sleep(0.5)
    print("\tThere is an inventory system in game. ")
    player_inventory.display_Inventory(person)
    sleep(0.5)
    print("\tYou can access the inventory whenever you're prompted this: \n")
    sleep(0.5)
    print("==================================================================")
    print(" I : Open Inventory\t E : Exit\t M:Move on ")
    print("==================================================================")
    sleep(0.5)
    print("Press Enter to continue ...")
    # Consume the input
    input()

# Test area :


# i1 = Inventory()
# i1.display_Inventory()
