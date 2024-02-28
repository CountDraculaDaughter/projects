from random import randint
import keyboard

messageout = ("Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", \
             "As I see it, yes", "Most likely", "Outlook good", "Signs point to yes", "Yes", "It is certain", \
             "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "Reply hazy, try again", \
             "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again")

message_count = [0] * len(messageout)
playAgain = True
while playAgain == True:
    print("Welcome Player to the Eight Ball Program")
    userInput = input("It is now time to clear your mind and ask your yes/no: ")
    print("Press any key to show the ball response")

    if keyboard.read_key():
        magicChoice = randint(0, 19)
        print(messageout[magicChoice])
        message_count[magicChoice] += 1
        print(f"Message \"{messageout[magicChoice]}\" has been displayed {message_count[magicChoice]} times")
    nextRound = input("Enter yes to play again, else type no: ")
    if nextRound == "no":
        playAgain = False

print("Messages that did not displayed:")
for pos in range(0, len(message_count) - 1):
    if message_count[pos] == 0:
        print(messageout[pos])
