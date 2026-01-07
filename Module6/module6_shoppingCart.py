'''
Colorado State University Global
( https://csuglobal.edu/academic-programs/graduate-degrees/masters-science-degree-artificial-intelligence-machine-learning )
MS - Artificial Intelligence and Machine Learning
Course: CSC500 - Principles of Programming
Module 6: Portfolio Milestone (Online Shopping Cart)
Professor: Dr. Steven A. Evans
Created by Mukul Mondal
February 21, 2025
'''

from os import system, name
from typing import List, Dict
import re
from datetime import date


def clearScreen():    
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


# This represents an item in the shopping store.
# This should not be part of the shopping Cart.
# This should be a component of the shopping Store.
class StoreItem:
    def __init__(self, name:str, desc:str, price:float):
        self.Name: str = name.lstrip().rstrip()         # Item Name
        self.Description: str = desc.lstrip().rstrip()  # Item Description
        self.Price: float = price                       # Item Price

# This represents the container of all items in the store
# This dictionary has Key as 'Item Name' and Value as 'Store item' object as defined above.
# This should not be part of the Cart.
# This should be a component of the Store.
itemNameStoreItem_dict: Dict[str,StoreItem] = {
    'nike romaleos': StoreItem('Nike Romaleos', 'Volt color, Weightlifting shoes', 189.0),
    'chocolate chips': StoreItem('Chocolate Chips', 'Semi-sweet', 3.0),
    'powerbeats 2 headphones': StoreItem('Powerbeats 2 Headphones', 'Bluetooth headphones', 128.0)
}

# Display all available items in the store.
def ShowStoreItems():
    print(" === Please see below our today's available items in the Store === ")
    itemCount = 1
    for key,value in itemNameStoreItem_dict.items():
        print(f"{itemCount}.\t{value.Name}\t@ ${value.Price}\t{value.Description}")
        itemCount += 1
    return

# Add new item in the store.
def AddNewStoreItem():
    newItemName = input("Please enter new item name: ").lstrip().rstrip()
    while len(newItemName) < 1 or newItemName in itemNameStoreItem_dict:
        newItemName = input("Try again with different new item name: ").lstrip().rstrip()

    newItemDescription = input("Please enter new item description: ").lstrip().rstrip()
    newItemPrice = 0.0
    validInput = False
    while not validInput and newItemPrice <= 0.0:
        try:
            newItemPrice = float(input('Enter the item price: '))
            validInput = True
        except ValueError:
            print('(Invalid Input) Please try again')

    itemNameStoreItem_dict[newItemName.lower()] = StoreItem(newItemName,newItemDescription,newItemPrice)    
    return


# This represents each item in the user ShoppingCart. It also shows default initialization.
class CartItem:
    def __init__(self):
        self.itemName = "defaultName"           # default itemName = "defaultName"
        self.itemCount = 1                      # default itemCount = 1
        self.itemPrice = 1.0                    # default itemPrice = 1.0
        self.Description = "defaultDescription" # default Descrition = "defaultDescription"

# This represents the Shopping cart.
class ShoppingCart:    
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items: List[CartItem] = [] # as stated in the problem, it should list. So, here I'll use above 'CartItem' object as each item in the list.
    def __init__(self,name:str,date:str):
        self.customer_name = name.lstrip().rstrip()
        self.current_date = date.lstrip().rstrip()
        self.cart_items: List[CartItem] = []

    # helper function to search an item in the cart(collection of 'CartItem' objects) by ItemName.
    def find_item_by_name(self, name:str):
        for item in self.cart_items:
            if re.search(name, item.itemName, re.IGNORECASE):
                return item
        return None

    # Adds an item to cart_items list. Has parameter ItemToPurchase.
    # To make it more user friendly, we'll assume ItemToPurchase is of type: StoreItem
    def add_item(self, ItemToPurchase: CartItem ):        
        itemToPurchaseName = ItemToPurchase.itemName.lstrip().rstrip()        
        if len(itemToPurchaseName) > 0 :
            existingCartItem = self.find_item_by_name(itemToPurchaseName)
            if existingCartItem == None:
                existingCartItem = CartItem()
                existingCartItem.itemPrice = itemNameStoreItem_dict[itemToPurchaseName.lower()].Price
                existingCartItem.Description = itemNameStoreItem_dict[itemToPurchaseName.lower()].Description
                existingCartItem.itemCount = ItemToPurchase.itemCount
                existingCartItem.itemName = itemToPurchaseName
                self.cart_items.append(existingCartItem) # new item added in the ShoppingCart                
            else:
                indx: int = self.cart_items.index(existingCartItem)
                self.cart_items[indx].itemCount = self.cart_items[indx].itemCount + ItemToPurchase.itemCount                
        return

    # Removes item from cart_items list. Has a string (an item's name) parameter.
    def remove_item(self, itemName:str ):
        itemName = itemName.lstrip().rstrip()
        if len(itemName) > 0:
            existCartItem = self.find_item_by_name(itemName)
            if existCartItem is not None:
                self.cart_items.remove(existCartItem)                    
            else:
                print("Item not found in cart.")
        return

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase.
    # If item Not found (by name) in cart, output this message: Item not found in cart.
    # If item found in cart, check if parameter has default values for description, price, and quantity. 
    #     If not, modify item in cart. Otherwise, nothing modified.
    # To make it more user friendly, we'll assume ItemToPurchase is of type: StoreItem
    def modify_item(self, ItemToPurchase: CartItem ):
        existCartItem = self.find_item_by_name(ItemToPurchase.Name.lstrip().rstrip())
        if existCartItem != None:
            self.cart_items.remove(existCartItem)
            existCartItem.Description = itemNameStoreItem_dict[existCartItem.itemName.lower()].Description
            existCartItem.itemPrice = itemNameStoreItem_dict[existCartItem.itemName.lower()].Price
            existCartItem.itemCount = ItemToPurchase.itemCount
            self.cart_items.append(existCartItem)
        else:
            print("Item not found in cart")        
        return

    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity), "@ ${:.2f} = ${:.2f}". format(self.item_price, (self.item_price * self.item_quantity)))
        return

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        totalCost = 0.0
        for anItem in self.cart_items:
            totalCost += anItem.itemPrice
        return totalCost

    # Outputs total of objects in cart. If cart is empty, output this message: SHOPPING CART IS EMPTY.
    def print_total(self):
        if len(self.cart_items) < 1:
            print('SHOPPING CART IS EMPTY')            
            return
        print(self.customer_name + "'s Shopping Cart - ", self.current_date)
        totalItems = 0
        for anItem in self.cart_items:
            totalItems += anItem.itemCount
        print("Number of Items: ", str(totalItems))
        totalCost = 0.0
        for anItem in self.cart_items:
            totalCost += (anItem.itemPrice * anItem.itemCount)
            print(anItem.itemName, str(anItem.itemCount), "@ ${:.2f} = ${:.2f}". format(anItem.itemPrice, (anItem.itemPrice * anItem.itemCount)))
        print("Total: ", "@ ${:.2f}".format(totalCost))
        return

    # Outputs each item's description.
    def print_descriptions(self):
        if len(self.cart_items) < 1:
            print('SHOPPING CART IS EMPTY')            
            return
        print(self.customer_name + "'s Shopping Cart - ", self.current_date)
        print("Item Descriptions")        
        for anItem in self.cart_items:            
            print(anItem.itemName, ": ", anItem.Description)        
        return
    
# Displays the menu for user action.
def print_menu():    
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")    
    return

# Read menu selection by the user.
def readUserSelection():
    userInput = ""
    while userInput != "arcioq" and len(userInput) != 1:
        userInput = input('Choose an option: ').lstrip().rstrip().lower()
    return userInput

# Handles an Item buy by the user
def buyOneItem():
    newItemName = input("Please enter the item name, you want to buy: ").lstrip().rstrip()
    while len(newItemName) < 1 or (newItemName in itemNameStoreItem_dict == False):
        newItemName = input("Please check the available store items and try again! Enter item name: ").lstrip().rstrip()
    
    howmany: int = 0
    validInput = False
    while howmany < 1 and validInput == False:
        try:
            howmany = int(input('How many of this item you want to buy? '))
            validInput = True
        except ValueError:
            print('(Invalid Input) Please try again')

    CartItemObj = CartItem()
    CartItemObj.itemName = newItemName
    CartItemObj.itemCount = howmany
    CartItemObj.Description = itemNameStoreItem_dict[newItemName.lower()].Description    
    return CartItemObj

# the main function that calls other functions and does the final work
def module6pm_shopping_cart():
    clearScreen()
    print("\n === Shopping Cart Demo ===")
    ShowStoreItems()
    #AddNewStoreItem()  # works ok
    #ShowStoreItems()
    
    print("\n")
    customerName = ""
    while len(customerName) < 1:
        customerName = input("Please enter customer name: ").lstrip().rstrip()
    ShoppingCart_obj = ShoppingCart(customerName, date.today().strftime("%B %d, %Y"))
    
    print_menu()
    userSelection = readUserSelection()
    while userSelection != 'q':
        if userSelection == 'a':  # a - Add item to cart
            print("Add item to cart:")
            newcartItem = buyOneItem()            
            ShoppingCart_obj.add_item(newcartItem)
        elif userSelection == 'r': # r - Remove item from cart
            removeItemName = ""
            while len(removeItemName) < 1:
                removeItemName = input("Please enter the item name, you want to remove from cart: ").lstrip().rstrip()
            ShoppingCart_obj.remove_item(removeItemName)
        elif userSelection == 'c': # c - Change item quantity
            changeItemName = ""
            while len(changeItemName) < 1:
                changeItemName = input("Please enter item name for which you want to change the quantity: ").lstrip().rstrip()
            foundCartItem = ShoppingCart_obj.find_item_by_name(changeItemName)
            if foundCartItem == None:
                print("This item not found in your current cart:")
            else:
                howmany: int = 0
                validInput = False
                while howmany < 0 and not validInput:
                    try:
                        howmany = int(input('How many of this item you want to keep? '))
                        validInput = True
                    except ValueError:
                        print('(Invalid Input) Please try again')
                ShoppingCart_obj.cart_items[ShoppingCart_obj.cart_items.index(foundCartItem,0)].itemCount = howmany
        elif userSelection == 'i': # i - Output items' descriptions
            ShoppingCart_obj.print_descriptions()
        elif userSelection == 'o':  # o - Output shopping cart
            ShoppingCart_obj.print_total()

        print("\nPlease Choose your next menu option: ")
        userSelection = readUserSelection()
        
    print("Thank you") # q - Quit
    return


if __name__ == "__main__":
    module6pm_shopping_cart()
