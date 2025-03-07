from os import system, name
from typing import List, Dict
import re
from datetime import date, datetime

# This is just a helper function to clear the screen
# This is not required, per requirement.
def clearScreen():    
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


# This represents an item in the shopping store.
# This should not be part of the shopping Cart.
# This should be a component of the shopping Store.
# This is not required, per requirement.
class StoreItem:
    def __init__(self, name:str, desc:str, price:float):
        self.Name: str = name.lstrip().rstrip()         # Item Name
        self.Description: str = desc.lstrip().rstrip()  # Item Description
        self.Price: float = price                       # Item Price

# This represents the container of all items in the store
# This dictionary has Key as 'Item Name' and Value as 'StoreItem' object as defined above.
# This dictionary has items initialized with default values.
# This should not be part of the Cart.
# This should be a component of the Store.
# This is not required, per requirement.
# I'll use these default values in 'modify_item()' method within 'Milestone 2'.
dict_StoreItems: Dict[str, StoreItem] = {
    'nike romaleos': StoreItem('Nike Romaleos', 'Volt color, Weightlifting shoes', 189.0),
    'chocolate chips': StoreItem('Chocolate Chips', 'Semi-sweet', 3.0),
    'powerbeats 2 headphones': StoreItem('Powerbeats 2 Headphones', 'Bluetooth headphones', 128.0)
}

# Display all available items in the store.
# This is not required, per requirement.
def ShowStoreItems():
    print(" === Please see below our today's available items in the Store === ")
    itemCount = 1
    for key,value in dict_StoreItems.items():
        print(f"{itemCount}.\t{value.Name}\t@ ${value.Price}\t{value.Description}")
        itemCount += 1
    return

# Add new StoreItem in the store. Works ok
# This is not required, per requirement.
def AddNewStoreItem():
    newItemName = input("Please enter new item name: ").lstrip().rstrip()
    while len(newItemName) < 1 or newItemName in dict_StoreItems:
        newItemName = input("Try again with different new item name: ").lstrip().rstrip()

    newItemDescription = input("Please enter new item description: ").lstrip().rstrip()
    newItemPrice = 0.0
    validInput = False
    while not validInput or newItemPrice <= 0.0:
        try:
            newItemPrice = float(input('Enter the item price: '))
            if newItemPrice > 0.0:
                validInput = True
        except ValueError:
            print('(Invalid Input) Please try again')

    dict_StoreItems[newItemName.lower()] = StoreItem(newItemName,newItemDescription,newItemPrice)    
    return

# Module 8: Portfolio Project
# Step 1: Build the ItemToPurchase class with the following specifications
class ItemToPurchase:
    def __init__(self):
        self.item_name: str = "none"    # default item_name = "none"
        self.item_price: float = 0.0    # default item_price = 0.0
        self.item_quantity: int = 0     # default  item_quantity = 0
        self.Description = ""           # this attribute mentioned in modify_item() method's requirement.
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = {self.item_price*self.item_quantity}")

# dictionary (storage) of purchased items
# key: 'item name', value: purchased 'ItemToPurchase' object
dict_purchasedItems: Dict[str,ItemToPurchase] = { }

# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
def purchaseOneItem(isMilestone1: bool = False, howmany: int = 1):
    newItemName = input("Enter the item name: ").lstrip().rstrip()
    while len(newItemName) < 1 or (newItemName.lower() in dict_purchasedItems):
        if newItemName.lower() in dict_purchasedItems:
            print("This item is already present in your cart!!")
        newItemName = input("(try again) Enter the item name: ").lstrip().rstrip()

    if isMilestone1 == False:
        newItemDesc = input("Enter the item description: ").lstrip().rstrip()
        while len(newItemDesc) < 1:
            newItemDesc = input("(try again) Enter the item description: ").lstrip().rstrip()
    
    itemPrice: float = 0.0
    validInput = False
    while validInput == False or itemPrice <= 0.0:
        try:
            itemPrice = float(input("Enter the item price: "))
            if itemPrice > 0.0:
                validInput = True
        except ValueError:
            print("(Invalid Input) Enter the item price: ")
        
    validInput = False
    while howmany < 1 or validInput == False:
        try:
            howmany = int(input("Enter the item quantity: "))
            if howmany > 0:
                validInput = True
        except ValueError:
            print("(invalid input) Enter the item quantity: ")

    itemPurchased = ItemToPurchase()
    itemPurchased.item_name = newItemName
    if isMilestone1 == False:
        itemPurchased.Description = newItemDesc
    itemPurchased.item_quantity = howmany
    itemPurchased.item_price = itemPrice
    dict_purchasedItems[newItemName.lower()] = itemPurchased
    return itemPurchased

# Step 3: Add the costs of the two items together and output the total cost.
def showTotalCosts(purchasedItems: List[ItemToPurchase]):
    print("\tTOTAL COST")
    totalCost: float = 0.0
    for oneItem in purchasedItems:
        totalCost = totalCost + (oneItem.item_price)*(oneItem.item_quantity)
        print(f"{oneItem.item_name} {oneItem.item_quantity} @ ${oneItem.item_price} = ${oneItem.item_price*oneItem.item_quantity}")
    print(f"Total: ${totalCost}")
    return


# Milestone 1
def Milestone1():   
    dict_purchasedItems.clear()
    print("\t Item 1")
    purchaseOneItem(isMilestone1=True)
    print("\t Item 2")
    purchasedItem = purchaseOneItem(isMilestone1=True)
    # purchasedItem.print_item_cost() # Step 1
    showTotalCosts(dict_purchasedItems.values())
    return

# Milestone 2
# This represents the Shopping cart.
class ShoppingCart:    
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items: List[ItemToPurchase] = [] # as stated in the problem, it should be list. So, here I'll use above 'ItemToPurchase' object as each item in the list.
    def __init__(self, name:str, date:str):
        self.customer_name = name.lstrip().rstrip()
        self.current_date = date.lstrip().rstrip()
        self.cart_items: List[ItemToPurchase] = []

    # helper function to search an item in the cart(collection of 'ItemToPurchase' objects) by ItemName.
    def find_item_by_name(self, name: str):
        for item in self.cart_items:
            if re.search(name, item.item_name, re.IGNORECASE):
                return item
        return None

    # Adds an item to cart_items list. Has parameter ItemToPurchase.
    # To make it more user friendly, we'll assume ItemToPurchase is of type: StoreItem
    def add_item(self, itemToPurchase: ItemToPurchase):
        itemToPurchaseName = itemToPurchase.item_name.lstrip().rstrip()        
        if len(itemToPurchaseName) > 0 and itemToPurchase.item_price > 0 and itemToPurchase.item_quantity > 0:
            existingCartItem = self.find_item_by_name(itemToPurchaseName)
            if existingCartItem == None:              
                self.cart_items.append(itemToPurchase) # new item added in the ShoppingCart
            else:  # existing item count updated in the ShoppingCart
                indx: int = self.cart_items.index(existingCartItem)
                self.cart_items[indx].item_quantity = self.cart_items[indx].item_quantity + ItemToPurchase.item_quantity                
        return

    # Removes item from cart_items list. Has a string (an item's name) parameter.
    def remove_item(self, itemName: str):
        itemName = itemName.lstrip().rstrip()
        if len(itemName) > 0 and len(self.cart_items) > 0:
            existCartItem = self.find_item_by_name(itemName)
            if existCartItem != None:
                self.cart_items.remove(existCartItem)
                del dict_purchasedItems[itemName.lower()]
            else:
                print("Item not found in cart.")
        return

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase.
    # If item Not found (by name) in cart, output this message: Item not found in cart.
    # If item found in cart, check if parameter has default values (as initialized in 'dict_StoreItems' earlier) for description, price, and quantity.
    #     If not, modify item in cart. Otherwise, nothing modified.    
    def modify_item(self, modifyingItem: ItemToPurchase ):
        if modifyingItem != None and len(self.cart_items) > 0:
            indx = next((i for i, x in enumerate(self.cart_items) if (lambda x: modifyingItem.item_name.lower() == x.item_name.lower()) ))
            if(indx >= 0): # 'modifyingItem' found in the 'cart_items list' at index 'indx'
                self.cart_items[indx].Description = dict_StoreItems[modifyingItem.item_name.lower()].Description
                self.cart_items[indx].item_price = dict_StoreItems[modifyingItem.item_name.lower()].Price
                self.cart_items[indx].item_quantity = 1 # default value not mentioned in the problem statement, logically assumed to be 1
            else:
                print("Item not found in cart")
        return

    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        totalItemCount: int = 0
        for anItem in self.cart_items:
            totalItemCount += anItem.item_quantity 
        return totalItemCount # len(self.cart_items)

    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity), "@ ${:.2f} = ${:.2f}". format(self.item_price, (self.item_price * self.item_quantity)))
        return

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        totalCost = 0.0
        for anItem in self.cart_items:
            totalCost += (anItem.item_price)*(anItem.item_quantity)
        return totalCost

    # Outputs total of objects in cart. If cart is empty, output this message: SHOPPING CART IS EMPTY.
    def print_total(self):
        if len(self.cart_items) < 1:
            print('SHOPPING CART IS EMPTY')            
            return
        print(self.customer_name + "'s Shopping Cart -", self.current_date)
        totalItems = 0
        for anItem in self.cart_items:
            totalItems = totalItems + anItem.item_quantity
        print("Number of Items:", str(totalItems))
        totalCost = 0.0
        for anItem in self.cart_items:
            totalCost += (anItem.item_price * anItem.item_quantity)
            print(anItem.item_name, str(anItem.item_quantity), "@ ${:.2f} = ${:.2f}". format(anItem.item_price, (anItem.item_price * anItem.item_quantity)))
        print("Total: ", "@ ${:.2f}".format(totalCost))
        return

    # Outputs each item's description.
    def print_descriptions(self):
        if len(self.cart_items) < 1:
            print('SHOPPING CART IS EMPTY')            
            return
        print(self.customer_name + "'s Shopping Cart -", self.current_date)
        print("\tItem Descriptions")        
        for anItem in self.cart_items:            
            print(anItem.item_name, ":", anItem.Description)
        return
    
# Step 5:
# Displays the menu for user action.
def print_menu():    
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")    
    return

# Read menu selection by the user. Step 5
# User has to enter option only within: 'a', 'r', 'c', 'i', 'o', 'q'
def readUserSelection():
    userInput = ""
    while len(userInput) != 1 or userInput not in "arcioq":
        userInput = input('Choose an option: ').lstrip().rstrip().lower()
    return userInput

# the main function that calls other functions and does the final work
def Milestone2():
    dict_purchasedItems.clear()
    print("\n === Shopping Cart Demo ===")
    ShowStoreItems()
    #AddNewStoreItem() # works ok
    #ShowStoreItems()  # works ok
    
    # Step 7 begins
    print("\n")
    customerName = ""
    userEnteredDate = ""
    while len(customerName) < 1:
        customerName = input("Enter customer's name: ").lstrip().rstrip()
    
    validInput = False    
    while validInput == False:
        try:
            userEnteredDate = (datetime.strptime(input("Enter today's date (format: February 27, 2025): "), "%B %d, %Y")).strftime("%B %d, %Y")
            if len(userEnteredDate) > 0:
                validInput = True
        except ValueError:
            print("(Invalid Input) Enter today's date (format: February 27, 2025)")    
    ShoppingCart_obj = ShoppingCart(customerName, userEnteredDate)
    
    print(f"Customer name: {ShoppingCart_obj.customer_name}")
    print(f"Today's date: {ShoppingCart_obj.current_date}\n")
    # Step 7 ends

    print_menu() # Step 5.
    userSelection = readUserSelection()
    while userSelection != 'q':
        if userSelection == 'a':  # a - Add item to cart. Step 8.
            print("ADD ITEM TO CART")
            newcartItem = purchaseOneItem()
            ShoppingCart_obj.add_item(newcartItem)
        elif userSelection == 'r': # r - Remove item from cart. Step 9.
            print("REMOVE ITEM FROM CART")
            removeItemName = ""
            while len(removeItemName) < 1:
                removeItemName = input("Enter name of item to remove:").lstrip().rstrip()
            ShoppingCart_obj.remove_item(removeItemName)
        elif userSelection == 'c': # c - Change item quantity. Step 10.
            print("CHANGE ITEM QUANTITY")
            changeItemName = ""
            while len(changeItemName) < 1:
                changeItemName = input("Enter the item name:").lstrip().rstrip()
            foundCartItem = ShoppingCart_obj.find_item_by_name(changeItemName)
            if foundCartItem == None:
                print("This item not found in your current cart:")
            else:
                howmany: int = 0
                validInput = False
                while howmany < 0 or validInput == False:
                    try:
                        howmany = int(input("Enter the new quantity:"))
                        if howmany > 0:
                            validInput = True
                    except ValueError:
                        print('(Invalid Input) Please try again')
                ShoppingCart_obj.cart_items[ShoppingCart_obj.cart_items.index(foundCartItem,0)].item_quantity = howmany
        elif userSelection == 'i': # i - Output items' descriptions
            print("\tOUTPUT ITEMS' DESCRIPTIONS")
            ShoppingCart_obj.print_descriptions()
        elif userSelection == 'o':  # o - Output shopping cart. Step 6
            print("\tOUTPUT SHOPPING CART")
            ShoppingCart_obj.print_total()

        print("\nPlease Choose your next menu option: ")
        userSelection = readUserSelection()
        
    print("Thank you") # q - Quit
    return


if __name__ == "__main__":
    clearScreen()
    print("===== Milestone1 =====")
    Milestone1()
    print("\n===== Milestone2 =====")
    Milestone2()