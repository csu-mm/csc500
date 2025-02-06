'''
Part 2:
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
'''

from os import system, name


def clearScreen():    
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


def getUserInput2DigitsHourTime(userMsg):        
    userInput2DigitHours = 0
    validInput = False
    while not validInput:
        try:
            userInput2DigitHours = int(input(userMsg))
            if userInput2DigitHours < 0 or userInput2DigitHours > 99:                
                print("(Invalid Input), try again! >>> ")
            else:
                validInput = True
        except ValueError:
            print("(Invalid Input), try again! >>> ")
    return userInput2DigitHours
    

# the main function that calls other functions and does the final work
def ct_part2():
    clearScreen()    
    currrentTime2DigitUserInput = getUserInput2DigitsHourTime("Please enter 2 digit hours for the current time: ")
    waitTime2DigitUserInput = getUserInput2DigitsHourTime("Please enter 2 digit hours for how long you want to wait: ")
    time2DigitAlarm = (currrentTime2DigitUserInput + waitTime2DigitUserInput)%24
    print('2 digit hour time when alarm will go off is: ', str(time2DigitAlarm))
    return

if __name__ == "__main__":
    ct_part2()
