# Jordan Drabek - CSC 152 - Lab assignment 4

# Lab 1
# Number Guessing game
# use random.randint(1, 10) to generate a random number.
# Create a loop that allows the user to guess the number up to 3 times.
# After each guess, tell the user whether their guess is too high, too low, or correct.
# If the user guesses the number or runs out of attempts, print an appropriate message.

import random

randnum = random.randint(1,10)
tries = 3
count = 1


while count <= tries:

    userattempt = int(input("Guess a number from 1 - 10: "))

    if userattempt > randnum:
        print("Your guess is too high")
        count = count + 1
    elif userattempt < randnum:
        print("Your guess is too low")
        count = count + 1
    else:
        print("You have chosen wisely")
        break
else:
        print("You have chosen poorly")


# Lab 2
# Ask the user to input a number to start the countdown.
# Use a while loop to decrement the number.
# Print the countdown until it reaches 1.

countdowninput = int(input("Enter a number to begin the countdown: "))

while countdowninput > 0:
     
     print (countdowninput)
     countdowninput = countdowninput - 1

else:
     print("Blast Off!")

# Lab 3

# Ask the user to input a number.
# Use a for loop to sum the numbers from 1 to the user’s input number.
# Print the total sum.

usernum = int(input("Put in a number: "))
totalsolve = 0

for numb1 in range(1, usernum + 1):
    totalsolve += numb1
    print(totalsolve)




