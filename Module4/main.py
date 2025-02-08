'''
Module 4: Portfolio Milestone:
Online Shopping Cart

Step 1: 
Build the ItemToPurchase class with the following specifications:
Attributes:
item_name (string)
item_price (float)
item_quantity (int)
Default constructor: Initializes item's name = "none", item's price = 0, item's quantity = 0
Method: print_item_cost()
Example of print_item_cost() output: Bottled Water 10 @ $1 = $10

Step 2: 
In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
'''

from os import system, name


def clearScreen():    
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


class ItemToPurchase:    
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
    
    def print_item_cost(self):  # output: Bottled Water 10 @ $1 = $10
        print(self.item_name, str(self.item_quantity), "@ ${:.2f} = ${:.2f}". format(self.item_price, (self.item_price * self.item_quantity)))
        return

def CreateOneItem():
    newItem = ItemToPurchase()

    # read user input for item_name
    newItem.item_name = input('Enter the item name: ').lstrip().rstrip()  
    while len(newItem.item_name) < 1:
        newItem.item_name = input('(Invalid Input)Tray again! Enter the item name: ').lstrip().rstrip()
    
    # read user input for item_price
    validInput = False
    while not validInput:
        try:
            newItem.item_price = float(input('Enter the item price: '))
            validInput = True
        except ValueError:
            print('(Invalid Input) Please try again')

    # read user input for item_quantity
    validInput = False
    while not validInput:
        try:
            newItem.item_quantity = int(input('Enter the item quantity: '))
            validInput = True
        except ValueError:
            print('(Invalid Input) Please try again')
        
    return newItem



# the main function that calls other functions and does the final work
def module4pm_shopping_cart():
    clearScreen()
    print("\n === Shopping Cart Demo ===")
    shopping_cart = []  # shopping cart, container of items purchased
    print("\n\tItem 1")
    shopping_cart.append(CreateOneItem())   # purchase item #1
    print("\n\tItem 2")
    shopping_cart.append(CreateOneItem())   # purchase item #2
    
    #display shopping cart, prices and total cost
    #print("\n === Purchased Items ===")
    print("\n\t TOTAL COST")
    totalcost = 0.0
    for item in shopping_cart:
        totalcost += item.item_price*item.item_quantity
        item.print_item_cost()
    
    print("Total: ${:.2f}".format(totalcost))
    return


if __name__ == "__main__":
    module4pm_shopping_cart()