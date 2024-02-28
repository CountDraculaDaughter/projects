import random

def main():
    user_wins = 0
    computer_wins = 0
    user_ties = 0
    user_total_wins = 0
    computer_total_wins = 0
    while user_total_wins < 2 and computer_wins < 2:
        while user_wins < 5 and computer_wins < 5:
            comp_choice = random.randint(1, 3)
            choice = user_input()
            user_choice, computer_choice, final_decision, user_wins, computer_wins, user_ties = \
                runSim(choice, comp_choice, computer_wins, user_wins, user_ties)
            printSim(user_choice, computer_choice, final_decision)
        print("The total score was: User got: " + str(user_wins) + " Computer got: " + 
            str(computer_wins) + " And the ties were: " + str(user_ties))
        if user_wins > computer_wins:
            user_total_wins += 1
        else:
            computer_total_wins += 1
        user_wins = 0
        computer_wins = 0
    print("The user had won: " + str(user_total_wins) + " The computer had won: " + 
        str(computer_total_wins))
    print("Goodbye, come back again")

def user_input():
    is_selection_valid = False
    while is_selection_valid == False:
        selection = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
        if selection.isdigit() and (int(selection) >= 1 and int(selection) <= 3) :
            return int(selection)
            is_selection_valid = True
        else:
            print("Invalid")


def runSim(userChoice, computerChoice, computerCounter, userCounter, ties):
    finalDecision = ""
    RPS = [
    ["", 
    "",
    "", 
    ""],
    ["", 
    "You tied. Try again!",
    "You lost. Try again!", 
    "Congrats, you won! Good bye."], 
    ["",
    "Congrats, you won! Good bye.",
    "You tied. Try again!",
    "You lost. Try again!"],
    ["",
    "You lost. Try again!", 
    "Congrats, you won! Good bye.", 
    "You tied. Try again!"]]
    Computer = ["",
    "The computer chose Rock",
    "The computer chose Paper",
    "The computer chose Scissors"]
    User = ["",
    "The user chose Rock",
    "The user chose Paper",
    "The user chose Scissors"]

    if RPS[userChoice][computerChoice] == "Congrats, you won! Good bye.":
        userCounter += 1
        finalDecision = "Congrats, you won! Good bye."
    elif RPS[userChoice][computerChoice] == "You tied. Try again!":
        ties += 1
        finalDecision = "You tied. Try again!"
    elif RPS[userChoice][computerChoice] == "You lost. Try again!":
        computerCounter += 1
        finalDecision = "You lost. Try again!"
    userChose = User[userChoice]
    computerChose = Computer[computerChoice]
    return userChose, computerChose, finalDecision, userCounter, computerCounter, ties

def printSim(userChoices, CompChoice, finalEnd):
    print(userChoices)
    print(CompChoice)
    print(finalEnd)


main()
