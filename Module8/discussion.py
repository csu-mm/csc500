from os import system, name
#from typing import Dict


def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


class MyClass:
    def __init__(self, public_value, protected_value, private_value):
        self.public_attribute = public_value
        self._protected_attribute = protected_value
        self.__private_attribute = private_value

    def public_method(self):
        return "This is a public method."

    def _protected_method(self):
        return "This is a protected method."

    def __private_method(self):
        return "This is a private method."

    def access_private_method(self):
        return self.__private_method()


def module8discussion():
    clearScreen()
    obj = MyClass(1, 2, 3)
    print(obj.public_attribute)  # This will work
    print(obj._protected_attribute)  # This will work, but it's not recommended to access protected members directly
  # print(obj.__private_attribute)  # This will raise an AttributeError
    print(obj.public_method())  # This will work
    print(obj._protected_method())  # This will work, but it's not recommended to call protected methods directly
 #  print(obj.__private_method())  # This will raise an AttributeError
    print(obj.access_private_method())  # This will work, as it accesses the private method from within the class
    return

if __name__ == "__main__":
    module8discussion()