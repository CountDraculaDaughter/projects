def main():
    empDict = {101:"McNally", 102:"Sama", 103:"Jones"}

    print("Welcome to Employee Dictionary")
    isRun = True
    while isRun == True:
        is_selection_valid = False
        while is_selection_valid == False:
            userInput = input("Press 1 to Add, 2 to Remove by ID, 3 to Update, 4 to Remove by Name, 5 to view, 0 to Exit: ")
            if userInput.isdigit() and (int(userInput) >= 0 and int(userInput) <= 5) :
                userChoice = int(userInput)
                is_selection_valid = True
            else:
                print("Not a valid input.")
        if userChoice == 0:
            isRun = False
            print("Thank you, goodbye")
        elif userChoice == 1:
            empDict = emp_add(empDict)
        elif userChoice == 2:
            empDict = emp_remove(empDict)
        elif userChoice == 3:
            empDict = emp_update(empDict)
        elif userChoice == 4:
            empDict = emp_removebyname(empDict)
        elif userChoice == 5:
            emp_view(empDict)


def emp_add(dic):
    isFine = False
    eIdInput = inputChecker()
    while isFine == False:
        if eIdInput in dic:
            print("ID already exists, please try again")
            eIdInput = inputChecker()
            isFine = False
        else:
            isFine = True
    eNameInput = input("Please enter employee last name: ")
    dic[eIdInput] = eNameInput
    return dic
def emp_remove(dic):
    isFine = False
    eIdInput = inputChecker()
    while isFine == False:
        if eIdInput in dic:
            print(f"Removing employee: {dic[eIdInput]}")
            dic.pop(eIdInput)
            isFine = True
        else:
            print("ID does not exist, please try again")
            eIdInput = inputChecker()
    return dic
def emp_update(dic):
    isFine = False
    eIdInput = inputChecker()
    while isFine == False:
        if eIdInput in dic:
            name = input(f"Updating {dic[eIdInput]}, Please enter new employee last name: ")
            dic[eIdInput] = name
            isFine = True
        else:
            print("ID does not exist, please try again")
            eIdInput = inputChecker()
    return dic
'''def emp_removebyname(dic):
    isFine = False
    name = input("Enter the employee's name that you wish to remove: ")

    isFound = False
    for key, value in dic.items():
        print (key, value)
        if value == name:
            del dic[key]
            isFound = True
    if isFound == False:
        print("Name did Not exist")
 #       name = input("Enter the employee's name that you wish to remove: ")
    return dic'''
def emp_view(dic):
    print("Currently in the Dictionary you have:")
    print(f"dictItems = {dic}")

def inputChecker():
    isInt = False
    while isInt == False:
        userInput = input("Enter the employee id: ")
        if userInput.isdigit():
            userInput = int(userInput)
            isInt = True
        else:
            print("Incorrect ID, please Try again, use numbers this time")
    return userInput
main()
