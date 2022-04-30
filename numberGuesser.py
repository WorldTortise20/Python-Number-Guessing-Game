from random import random


#importing the random class
import random
chosenNumber = random.randint(1,9)
chances = 4
while chances > 0:
    yourChoice = int(input("Guess the number! Pick any whole integer from 1-9! Your choice:"))
    if(yourChoice==chosenNumber):
        print("Well played! The number was indeed "+str(chosenNumber)+"!")
        break
        #Must make input into string to concatenate 
    elif(yourChoice>chosenNumber):
        print("Too high of a guess! Pick a number lower than "+str(yourChoice)+"!")
        chances = chances-1
    elif(yourChoice<chosenNumber):
        print("Too low of a guess! Pick a number high than "+str(yourChoice)+"!")
        chances = chances-1
    if(chances==0):
        print("Sorry, the number was "+str(chosenNumber))