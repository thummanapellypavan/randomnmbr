# randomnmbr
number guessing code 
import random

random_number = random.randint(1, 100)
win = False
turns = 0

while win == False:
    your_guess = int(input("Enter a number between 1 and 100: "))
    turns += 1
    
    if random_number == your_guess:
        print("You won!")
        print("Number of turns you have used:", turns)
        win = True
        break
    else:
        if random_number > your_guess:
            print("Your guess was low. Please enter a higher number.")
        else:
            print("Your guess was high. Please enter a smaller number.")

