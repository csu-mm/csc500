
'''
Part 1:
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user 
for the inches of rainfall for that month. After all iterations, the program should display the number of months, 
the total inches of rainfall, and the average rainfall per month for the entire period.
'''

from os import system, name
import numpy as np

monthsofyear = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'])

def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return

def getUserInputMonthRainfall(userMsg):
    inputValue = 0.0
    validInput = False
    while not validInput:
        try:
            inputValue = float(input(userMsg))
            if inputValue < 0:
                print("(Invalid Input), try again!")
            else:
                validInput = True
        except ValueError:
            print("(Invalid Input), try again!")
    return inputValue


def calculateRainfall():
    clearScreen()
    howManyYears = 0
    howManyMonths = 0
    totalRainfall = 0.0     
    
    validInput = False
    while not validInput:
        try:
            howManyYears = int(input("Please enter how many years to consider: "))
            if howManyYears < 0:
                print("(Invalid Input), try again!")
            else:
                validInput = True
        except ValueError:
            print("(Invalid Input), try again!")
    
    year = 1
    while( year <= howManyYears ):
        print("\tRainfall in year: ", str(year))
        for month in monthsofyear:            
            totalRainfall += getUserInputMonthRainfall("Please enter the rainfall in the month " + month + ": ")
        howManyMonths += 12
        year += 1
    
    print(" === Rainfall calculation for total Years: ", str(howManyYears), " === ")
    print("Total months: ", str(howManyMonths))    
    print("Total rainfall: ", "%.2f" % (totalRainfall), " inch")
    print("Average rainfall: ", "%.2f" % (totalRainfall/howManyMonths), " inch per month")
    return

if __name__ == "__main__":
    calculateRainfall()
