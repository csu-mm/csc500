'''
Part 2:
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
'''


from os import system, name
from datetime import datetime, timedelta


def clearScreen():    
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')

# Get current system date, time
def getCurrentLocalDatetime():        
    now = datetime.now()
    hour = now.strftime("%H") # Get the hour and date
    date = now.strftime("%d day of %B in the year %Y")    
    print("It is hour", hour, "of the", date) # Show current date/time
    return now

# Calculate the date, time after the waiting hours
def calculateNewDatetime(currentTime, hoursToWait):    
    newTime = currentTime + timedelta(hours=hoursToWait) # Calculate the new time    
    hour = newTime.strftime("%H") # Get the hour and date
    date = newTime.strftime("%d day of %B in the year %Y")    
    print("After", hoursToWait, "hours, it will be hour", hour, "of the", date)   # show the result


# the main function that calls other functions and does the final work
def ct_part2():
    clearScreen()
    curTime = getCurrentLocalDatetime()
    print("How many whole hours would you like to wait? >>> ", end='') # take user input
    validInput = False
    while not validInput:        
        try:
            hoursToWait = int(input())
            validInput = True
        except ValueError:
            print("(Invalid Input), try again! How many whole hours would you like to wait? >>> ", end='')
            pass
    
    calculateNewDatetime(curTime, hoursToWait) # Calculate new datetime

if __name__ == "__main__":
    ct_part2()
