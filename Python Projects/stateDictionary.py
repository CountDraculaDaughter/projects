# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#load items from the txt file to a list
def loadItems():
    # Use a breakpoint in the code line below to debug your script.
    file = open('stateinfo7.txt', 'r') #open file
    lines = file.readlines() #read lines
    stateList = [] #state list to return
    for line in lines: #read lines and determine action loop
        if len(line) > 4: #checks size for the case of blank spaces
            line = line.split(';') #split information
            line[0] = line[0].strip() #strip split one of extra info
            line[1] = line[1].strip() #strip split two of extra info
            line[2] = line[2].strip() #strip split three of extra info
            line[3] = line[3].strip() #strip split four of extra info
            stateList.append(line) #append the lines to the list
    return stateList #return list
    file.close() #close file
#Function that displays items
def displayItems(states):
    print('''Abbrev.#	        Name    		           Capital			Population
========	======================         ==================	================''') #Multi-line code to display the information
    for state in states: #for loop to read info from the list and display it also uses fstring to format information
        print(f"{state[0]:<12}{state[1]:<31}{state[2]:<21}{state[3]}")
#Function to build a dictionary
def buildDict(states):
    stateDict = {} #declare empty stateDict
    for state in states: #read individual states from the list
        stateDict[state[0]] = [state[1], state[2], state[3]] #adds the key state[0] from the list and then the rest are values, state[1], state[2], state [3]
    return stateDict #returns the dictionary
#Function to write to file
def writeFile(stateDict):
    writeableFile = open('IT209_A1output.txt', 'a') #writeable file "IT209_A1output.txt" with the append key
    for state in stateDict: #read lines from the stateDict
        if stateDict[state][0] == "Wyoming": #special case of the if statement to avoid having the new line after Wyoming
            writeableFile.write(f"{stateDict[state][0]},{stateDict[state][1]},{stateDict[state][2]}") #no newline, prevents that from happening, writes Wyoming, its capital, and its population to writefile
        else: #if not wyoming, go here
            writeableFile.write(f"{stateDict[state][0]},{stateDict[state][1]},{stateDict[state][2]}  \n") #write the states and their info to the writeFile, it has state name, capital, and population and then uses new line to allow the others to be written
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stateList = loadItems()
    displayItems(stateList)
    SD = buildDict(stateList)
    writeFile(SD)
