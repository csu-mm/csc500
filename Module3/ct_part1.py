'''
Part 1:
Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food and then calculate 
the amounts with an 18 percent tip and 7 percent sales tax. 
Display each of these amounts and the total price.
'''

from os import system, name
from datetime import datetime, timedelta


def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')

# define menu. I'll use dictionary to store menu. Key: food item name, Value: Price for that item.
# following is the menu with default food items.
# I've also provided function to add/update menu item: addNewItemToMenu() 
menu_dict = {    
    "eggsalad": 10.00,
    "hamburger": 13.50,
    "tunasalad": 14.00,
    "beefburger": 13.50,
    "steakburger": 13.50,
    "caesarsalad": 13.50,
    "cheeseburger": 11.50,
    "gardensalad": 12.50,
    "chickensalad": 12.50,
    "cubansandwich": 11.50,
    "denversandwich": 12.00,    
    "gerbersandwich": 11.50,
    "chickensandwich": 10.50    
}

# Show menu
def ShowMenu():
    print(" === Please see below our today's menu === ")
    for key,value in menu_dict.items():
        print(f"{key}\t${value}")
    return
    

# This function allows the restruant owner to add/update the menu item
def addNewItemToMenu():
    # user input: read new menu item name from customer input
    newMenuItemName = input("Please enter item name?: ").rstrip().lstrip().lower()
    #validInput = False
    while len(newMenuItemName) < 1 or newMenuItemName.isnumeric():
        newMenuItemName = input("(Invalid Input), please try again!: ").rstrip().lstrip().lower()        
    
    # user input: read new menu item price from user input    
    newMenuItemPrice = 0.0
    validInput = False
    while not validInput:        
        try:
            newMenuItemPrice = float(input("Please enter new item price?: "))
            if newMenuItemPrice == 0.0:
                print("(Invalid Input), please try again!")
                validInput = False
            else:
                validInput = True
        except ValueError:
            print("(Invalid Input), please try again!")
            validInput = False

    # add or update the new menu item in menu dictionary
    menu_dict[newMenuItemName] = newMenuItemPrice



# define one customer order. 
# I'll use dictionary to store one customer order. Key: food item name, Value: how many of this item ordered.
# initially it should be empty.
aCustomerOrder_dict = {}

# define all customers order. 
# I'll use dictionary to store all customer order. Key: customer name, Value: customer order dictionary.
allCustomerOrder_dict = {}

# take one customer order
def GetCustomerOrder():
    print(" === Accepting Customer Order === ") 
    print("Hello sir! Welcome, My name is abc...") 
    customerName = input("Your name, please? ").rstrip().lstrip().lower() # get customer name
    while len(customerName) < 1:
        customerName = input("Your name, please? ").rstrip().lstrip().lower()
    
    validInput1 = False
    itemName = ""
    while not validInput1:        
        validOrderName = False
        while not validOrderName: 
            itemName = input("What do you like to order? ").rstrip().lstrip().lower()
            if menu_dict.get(itemName) is None:  # check if the ordered item exists in the restruant menu
                validOrderName = False
                print("Say again, please!")
            else:
                validOrderName = True
                    
        #if itemName is present in menu_dict:  #valid Order name
        takeOrderMsg = "How many '" + itemName + "' you want?: "
        validInput2 = False
        while not validInput2:
            try:                
                orderItemCount = int(input(takeOrderMsg))
                if orderItemCount < 1:
                    print("Please try again!")
                    validInput2 = False                
                else:   # valid Order name and order item count
                    validInput2 = True
                    aCustomerOrder_dict[itemName] = orderItemCount
            except ValueError:
                    validInput2 = False
                    print("Please try again!")                
        
        #allCustomerOrder_dict[customerName] = aCustomerOrder_dict    
        moreItems = input("(yes/no) Would you like to order some more items from our menu! ").rstrip().lstrip().lower()
        while moreItems != "no" and moreItems.lower() != "yes":
            moreItems = input("(yes/no) Would you like to order some more items from our menu! ").rstrip().lstrip().lower()
        if moreItems == "yes":
            validInput1 = False
        else:
            allCustomerOrder_dict[customerName] = aCustomerOrder_dict
            print("Received order from the New Customer: ", customerName)
            validInput1 = True
    return        

# take all customers order
def GetAllCustomerOrders(customerCount):
    print("\n")
    if customerCount < 1:
        return
    while customerCount > 0:
        GetCustomerOrder()
        customerCount -= 1
        print("\n")
    return


# now, we've all customers order in the dictionary: allCustomerOrder_dict, where 'customer name' is the key
# and all orders for that customer is allCustomerOrder_dict["customer name"], which is again another dictionary,
#   'ordered item name' is the key and 'ordered item count' is the value.
# or len(allCustomerOrder_dict) < 1

def GetCustomerBill(customerName):
    print(" === Preparing Customer Bill === ")
    if len(customerName.rstrip().lstrip()) < 1 or allCustomerOrder_dict.get(customerName.rstrip().lstrip().lower()) is None:
        print("No Customer found")
        return
    print("Bill for Customer: ", customerName)
    totalcost = 0.0
    print("Item name:\t\tItem count:\tCost:")
    for key,value in allCustomerOrder_dict[customerName.rstrip().lstrip().lower()].items():        
        print(key + "\t\t" + str(value) + "\t\t" + str(value*menu_dict[key]))
        totalcost += value*menu_dict[key]
    
    # add 18 percent tip and 7 percent sales tax.
    print("Sales Tax @7%: $", "%.2f" % (totalcost*0.07))
    print("Tips:          $", "%.2f" % (totalcost*0.18))
    totalcost += (0.18+0.07)*totalcost    
    print("Total bill of ",customerName.rstrip().lstrip()," is:\t $", "%.2f" % totalcost)
    return


# Raise Bill to all customers
def RaiseBillToAllCustomers():
    print("\n")
    while len(allCustomerOrder_dict) > 0:    
        # we've customer to pay the bill
        # ask customer name
        billingcustomerName = input("Enter customer name for Bill: ").rstrip().lstrip().lower()
        while len(billingcustomerName) < 1 or allCustomerOrder_dict.get(billingcustomerName) is None:
            billingcustomerName = input("Try again, Enter customer name for Bill:").rstrip().lstrip().lower()

        # raise this customer's bill
        GetCustomerBill(billingcustomerName)

        # remove this customer's from customer collection
        del allCustomerOrder_dict[billingcustomerName]
    return


def ct_part1():
    clearScreen()
    print("Module 3 CT -- Part1 -- ")
    ShowMenu()
    
    # this variable holds the current number of the customer.
    # should be updated as new customer comes in. 
    currentCustomertCount = 1 # to meet the requirement as defined in the Problem

    # get orders for all all customers
    GetAllCustomerOrders(currentCustomertCount) 
    
    # when customer pays the bill
    RaiseBillToAllCustomers()

    return


if __name__ == "__main__":
    ct_part1()
