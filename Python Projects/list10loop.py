counter = 0
userList = []
while counter != 10:
    counter += 1
    userInput = int(input("Enter your number here: "))
    userList.append(userInput)
highest = userList[0]
lowest = userList[0]
for num in userList:
    if highest < num:
        highest = num
    if lowest > num:
        lowest = num
print(f"The highest number is {highest}")
print(f"The lowest number is {lowest}")
