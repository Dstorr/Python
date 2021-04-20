#Generating Random Numbers
import random

print("The game is heads or tails.")
coinToss = random.randint(0,1)
if coinToss == 1:
    print("You got, Tails")
else:
    print("You got, Heads")
    
print("\n")

#Rolling Dice
print("Roll a six-sided dice")
dice = random.randint(1,6)
if dice == 1:
    print("One")
elif dice == 2:
    print("Two")
elif dice == 3:
    print("Three")
elif dice == 4:
    print("Four")
elif dice == 5:
    print("Five")
elif dice == 6:
    print("Six")
    
print("\n")

#lucky Seven
print("This game is called Lucky Seven")
print("What is your name?")
name = input()
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print("Dice rolled: ", dice1, dice2)
Total = dice1 + dice2
print("Total: ", Total)
if Total == 7:
    print(name, "you win.")
else:
    print(name, "you lost.")

print("\n")

#Number between 1 and 20
print("This program will give you a number between 1 and 20")
numberGen = random.randint(1,20)

print("What number do you think it is?")
number = int(input())

if number == numberGen:
    print("You chose the right number")
elif number > numberGen:
    print("Your number is too large")
elif number < numberGen:
    print("Your number is too small")

