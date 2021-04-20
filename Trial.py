import random

#Instructions
print("Rock Paper Sicssors Game")
print("Give user input")
print("Computer Input")
print("\n")

#Number Code
# 0 = Rock
# 1 = Paper
# 2 = Scissors

#User input
user_input = int(input("Enter your number:")) 

#Computer Input
computer = random.randint(0,3)

print(user_input, "user choice")
print(computer, "computer choice")

#Draw
if user_input == computer:
    print("It was a draw")
    
    #Rock greater 
if user_input > 1:
    print(user_input, "User Wins")
elif user_input < 1:
    print(user_input, "Computer Wins")
elif user_input < 2:
    print("User win")

    
    
    
    
    