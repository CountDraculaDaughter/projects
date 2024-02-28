#Main function that runs code
def main():
    food, name, place, animal, profession, verb, things, clothing, verb2 = userInput()
    madlib(food, name, place)
    madlib2(animal, profession)
    madlib3(verb, things, clothing, verb2)
#Function so that we can collect user input
def userInput():
    food = input("Pick a food to use in this madlib: ")
    name = input("Pick a name to use in this madlib: ")
    place = input("Pick a place to use for this madlib: ")
    animal = input("Pick an animal to use in this madlib: ")
    profession = input("Pick a profession to use in this madlib: ")
    verb = input("Pick a verb to use in this madlib: ")
    things = input("Pick a thing to use in this madlib: ")
    clothing = input("Pick a clothing items to use in this madlib: ")
    verb2 = input("Pick a second verb to use in this madlib: ")
    return food, name, place, animal, profession, verb, things, clothing, verb2
def madlib(fd, nm, pl):
    nm = nm.capitalize()
    pl = pl.capitalize()
    print(f"\n\"Say {fd}\", the photographer said as the camera flashed! {nm} and I had gone to \n{pl} to get our photos taken on my birthday.\n")
def madlib2(an, prof):
    an = an.upper()
    prof = prof.upper()
    print(f"The first photo we really wanted was a picture of us dressed as {an} pretending \nto be a {prof}.\n")
def madlib3(vb, th, ct, vb2):
    th = th.lower()
    ct = ct.lower()
    vb2 = vb2.swapcase()
    print(f"When we {vb} the second photo, it was exactly what I wanted.  We both looked like {th} wearing {ct} and {vb2}\n")
main()
