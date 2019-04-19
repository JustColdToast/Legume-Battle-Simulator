# Written by Kanwarpal, JustColdToast
# This file is responsible for creating creatures from user input, based off of the object types present creatureScripts
# Statements to import classes from Scripts directory
from Scripts.creatureScript import *
# General import statements
import random  # Currently not used

# Main code, this allows user to build two creatures and make them fight
print("Welcome to creature-fighter version 1")
print("Let's build your first creature")

# Building the first creature
while True:
    firstType = input("What type do you want? Fire, Water, or Earth?: ")
    if firstType.lower() == "fire":
        creatureOne = fireType(input("Creature Name?: "),
                               int(input("Base Health?: ")),
                               int(input("Base Speed?: ")),
                               int(input("Base Attack?: ")),
                               int(input("Base Defense?: ")), 0)
        break
    elif firstType.lower() == "water":
        creatureOne = waterType(input("Creature Name?: "),
                               int(input("Base Health?: ")),
                               int(input("Base Speed?: ")),
                               int(input("Base Attack?: ")),
                               int(input("Base Defense?: ")), 0)
        break
    elif firstType.lower() == "earth":
        creatureOne = earthType(input("Creature Name?: "),
                               int(input("Base Health?: ")),
                               int(input("Base Speed?: ")),
                               int(input("Base Attack?: ")),
                               int(input("Base Defense?: ")), 0)
        break
    else:
        print("This is not a valid type, try again")

# Building the Second creature
print("Let's build your second creature")
while True:
    firstType = input("What type do you want? Fire, Water, or Earth?: ")
    if firstType.lower() == "fire":
        creatureTwo = fireType(input("Creature Name?: "),
                               int(input("Base Health?: ")),
                               int(input("Base Speed?: ")),
                               int(input("Base Attack?: ")),
                               int(input("Base Defense?: ")), 0)
        break
    elif firstType.lower() == "water":
        creatureTwo = waterType(input("Creature Name?: "),
                               int(input("Base Health?: ")),
                               int(input("Base Speed?: ")),
                               int(input("Base Attack?: ")),
                               int(input("Base Defense?: ")), 0)
        break
    elif firstType.lower() == "earth":
        creatureTwo = earthType(input("Creature Name?: "),
                               int(input("Base Health?: ")),
                               int(input("Base Speed?: ")),
                               int(input("Base Attack?: ")),
                               int(input("Base Defense?: ")), 0)
        break
    else:
        print("This is not a valid type, try again")

print("It's time to B A T T L E !")
# Insert battle code here
