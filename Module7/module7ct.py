from os import system, name
from typing import Dict



def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    return


dict_CourseID_RoomNumber: Dict[str,str] = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

dict_CourseID_Instructor: Dict[str,str] = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

dict_CourseID_MeetingTime: Dict[str,str] = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# requirement observations:
# 1. dictionary all keys are capitalized

def module7ct():
    clearScreen()
    # user enter a CourseID
    #print(f"Valid CourseIDs are: {", ".join(list(dict_CourseID_MeetingTime.keys()))}")
    print("Valid CourseIDs are: CSC101, CSC102, CSC103, NET110, COM241")
    inputCourseID = input("Please enter CourseID: ").lstrip().rstrip().upper()
    while (len(inputCourseID) < 1) or (inputCourseID not in dict_CourseID_MeetingTime):
        inputCourseID = input("Invalid input, try again. Enter the CourseID: ").lstrip().rstrip().upper()
    print(f"CourseID: {inputCourseID}\tRoom number: {dict_CourseID_RoomNumber[inputCourseID]}\tMeeting time: {dict_CourseID_MeetingTime[inputCourseID]}")
    return


if __name__ == "__main__":
    module7ct()