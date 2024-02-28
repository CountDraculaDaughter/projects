def main():
    meal = inputMeal()
    tippedFood = calcTip(meal)
    taxFood = calcTax(meal)
    totalFood = calcTotal(tippedFood, taxFood, meal)
    printTotal(totalFood)

def inputMeal():
    meal = float(input("Input the cost of the meal in the following format, XX.X: "))
    return meal

def calcTip(MealCost):
    tip = 0.0
    if MealCost >= 0.01 and MealCost <= 5.99:
        tip = 0.1
    elif MealCost >= 6.0 and MealCost <= 12.0:
        tip = 0.13
    elif MealCost >= 12.01 and MealCost <= 17.0:
        tip = 0.16
    elif MealCost >= 17.01 and MealCost <= 25.0:
        tip = 0.19
    elif MealCost >= 25.01:
        tip = 0.22
    CalcTips = MealCost * tip
    return CalcTips

def calcTax(FoodPrice):
    tax = 0.06
    taxedFood = FoodPrice * tax
    return taxedFood

def calcTotal(TaxFood, TipFood, MealCost):
    return TaxFood + TipFood + MealCost

def printTotal(TotalFood):
    newFood = round(TotalFood, 2)
    print ("Your total meal cost is:", newFood)

main()
