def openFile():
    try:
        fp = open("Hands-on15data.txt","r")
    except IOError:
        print("File not found")
        exit
    return fp

def main():
    fp = openFile()
    linelist = fp.readlines()
    nfp = open("av_controlbreak.txt","w")
    nfp.write("\t\tSales Report by State\t\t \n")
    nfp.write("Store Number\tState\tSales \n")
    nfp.write("===================================\n")
    currentState = ""
    stateTotal = 0
    for line in linelist:
        storeNum, state, revenue = line.split(" ")
        if state != currentState and currentState != "":
            record2 = (f"Total sales for {state}: ${stateTotal} ")
            nfp.write(record2 + "\n")
            stateTotal = 0
        currentState = state
        stateTotal += float(revenue)
        record = (f"{storeNum}\t\t\t\t{state}\t\t${revenue}")
        nfp.write(record +"\n")
    fp.close()
    nfp.close()
main()
