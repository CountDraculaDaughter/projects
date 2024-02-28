#Validation Method 1
grade = input("Enter your grade here: ")
grade = grade.upper()
while grade.upper() not in ("A","B", "C", "D", "F"):
    print("Try again")
    grade = input("Enter your grade here: ")
    grade = grade.upper()
if grade == "A" or grade == "B" or grade == "C":
    print("You passed")
elif grade == "D" or grade == "F":
    print("You failed")
else:
    print("Try again")
#Validation Method 2
while True:
    try:
        gradeNum = int(input("Enter your number grade: "))
    except:
        print("Try again")
    else:
        if gradeNum > 90:
            print("Great Job")
            break
        else:
            print("Study more")
            break
