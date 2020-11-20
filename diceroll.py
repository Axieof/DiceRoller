#Program by Pritheev
#Dice Roller

import random

#Variable Initialization
Loop = True
DiceSet = False

def MainMenu():
    print("========================")
    print("[1] Choose Dice Size")
    print("[2] Roll Dice")
    print("[0] Exit")
    print("========================")

def CoolDice(Number):
    print("+++++")
    print("+ {0} +".format(Number))
    print("+++++")
    print()

while(Loop):
    MainMenu()
    print()
    Options = int(input("Enter option: "))
    print()

    if (Options == 0):
        print("========================")
        print("Exiting...")
        print("========================")
        Loop = False
        break

    elif (Options == 1):
        print("========================")
        print("Option [1] Selected")
        print("========================")
        print()
        DiceSides = int(input("Enter number of sides for dice: "))
        print()
        DiceSet = True

    elif (Options == 2):
        print("========================")
        print("Option [1] Selected")
        print("========================")
        print()

        if (DiceSet):
            randomNum = random.randint(1, DiceSides)

            if (DiceSides < 10):
                CoolDice(randomNum)
            else:
                print(randomNum)
                print()
        else:
            print("Set a dice first!")
            print()