from os import system, name
from typing import List, Dict


def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return

# print(f"{itemCount}.\t{value.Name}\t@ ${value.Price}\t{value.Description}")
dict1 = {'a': 1, 'b': 2, 'c': 3}

def showKevValuePairs(dict : Dict[str,int]):
    for key,value in dict.items():
        print(f"{key} : {value}")
    return

list1 = [5, 8, 10]
def showList(list1 : List[int]):
    print(list1)
    return

def module6_discussion():
    showKevValuePairs(dict1)
    showList(list1)
    list1.append(6)
    showList(list1)
    return

if __name__ == "__main__":
    module6_discussion()