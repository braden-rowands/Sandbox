"'Braden'"
userInput = input("Please enter your name")
while len(userInput) < 1:
    userInput = input("Please enter a valid name")
print(userInput[::2])