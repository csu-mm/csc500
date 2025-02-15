'''
Part 2:
The CSU Global Bookstore has a book club that awards points to its students based on the number of 
books purchased each month. The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month 
and then display the number of points awarded.
'''
# Assumptions:
# If a customer purchases 1 book, they earn 0 points. Same as 0 book.
# If a customer purchases 3 books, they earn 5 points. Same as 2 books.
# If a customer purchases 5 books, they earn 15 points. Same as 4 books.
# If a customer purchases 7 books, they earn 30 points. Same as 6 books.


from os import system, name


def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return

def calculateAwardPoint():
    clearScreen()
    bookPurchsedCount = 0
    validInput = False
    while not validInput:
        try:
            bookPurchsedCount = int(input("Enter how many books you have purchased this month: "))
            if bookPurchsedCount < 0:
                print("(Invalid Input), try again!")
            else:
                validInput = True
        except ValueError:
            print("(Invalid Input), try again!")

    if bookPurchsedCount > 7:
        print("You've earned 60 award points")
    elif bookPurchsedCount > 5:
        print("You've earned 30 award points")
    elif bookPurchsedCount > 3:
        print("You've earned 15 award points")
    elif bookPurchsedCount > 1:
        print("You've earned 5 award points")
    else:
        print("You've earned 0 award points")
    return


if __name__ == "__main__":
    calculateAwardPoint()