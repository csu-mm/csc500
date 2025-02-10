
from os import system, name

def clearScreen():    
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return

    
def module5discussion():  #
    
    #examples:
    a = 2
    b = "abc"
    flag = True
    #example1:
    if a > 1 or b=="ab":  # returns 'True'
        print("example1: Combined condition(s) result is: True")
    else:
        print("example1: Combined condition(s) result is: False")

    #example2:
    if a > 1 and b=="ab":  # returns 'False'
        print("example2: Combined condition(s) result is: True")
    else:
        print("example2: Combined condition(s) result is: False")

    #example3:
    if a == 2 and b=="abc":  # returns 'True'
        print("example3: Combined condition(s) result is: True")
    else:
        print("example3: Combined condition(s) result is: False")

    #example4:
    if a == 2 or b=="ab" or False:  # returns 'True'
        print("example4: Combined condition(s) result is: True")
    else:
        print("example4: Combined condition(s) result is: False")

    #example5:
    if flag or (a == 2 or b =="ab"):  # returns 'False'
        print("example5: Combined condition(s) result is: True")
    else:
        print("example5: Combined condition(s) result is: False")

    # execution results
    #example1: Combined condition(s) result is: True
    #example2: Combined condition(s) result is: False
    #example3: Combined condition(s) result is: True
    #example4: Combined condition(s) result is: True
    #example5: Combined condition(s) result is: False

    return
    


if __name__ == "__main__":
    module5discussion()