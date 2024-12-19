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
