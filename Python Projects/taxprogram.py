#variables to calculate
global totalSale
totalSale = 0
global countyTax
countyTax = 0.0
global stateTax
stateTax = 0.0
# Left blank for spacing
def main(): #runs code
    printData()
def inputData(): #input monthly sales
    global totalSale
    totalSale = float(input("Enter the total sales for the month $"))
    #print(totalSale)
def calcCounty(): #calculate county tax
    global totalSale
    global countyTax
    countyTax = totalSale * 0.02
    print("The county tax is $ " + str(countyTax))
def calcState(): #calculate state tax
    global totalSale
    global stateTax
    stateTax = totalSale * 0.04
    print("The state tax is $ " + str(stateTax))
def totalTax(): #calculate all the stupid taxes
    global stateTax
    global countyTax
    totalTax = stateTax + countyTax
    print("The total tax is $ " + str(totalTax))
def printData(): #print data
    print("Welcome to the total tax calculator program")
    inputData()
    calcCounty()
    calcState()
    totalTax()
main()
