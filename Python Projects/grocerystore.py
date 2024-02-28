def main():
    endProgram = "no"
    while endProgram == "no":
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printInfo(totalBottles, totalPayout)
        endProgram = input(f"\nDo you want to end the program? (Enter yes or no): ")
        print("")
def getBottles():
    todayBottle = 0
    totalBottle = 0
    counter = 1
    while counter <= 7:
        todayBottle = int(input("Enter the number of bottles for today: "))
        totalBottle = totalBottle + todayBottle
        counter += 1
    return totalBottle
def calcPayout(TB):
    totalPayout = TB * 0.1
    totalPayout = round(totalPayout, 2)
    return totalPayout
def printInfo(TB, TP):
    print("The total number of bottles collected is: " + str(TB))
    print("The total payed out is $ " + str(TP))
main()
