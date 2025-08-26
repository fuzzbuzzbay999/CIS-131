3# cis131_lab_guess_the_number.py CIS 131 - lab 2
# Declan Juliano
# Date: 8/26/2025
# This program is a "guess the number" game where the user tries to guess a randomly generated number between 1 and 1000 in 10 tries or less.

from random import randint
num=int(randint(1,1000))
guess=0
Gcount=0
while guess!=num:
    guess=int(input("Enter your guess between 1 and 1000: "))
    if guess<num:
        print("Too low, try again")
    elif guess>num:
        print("Too high, try again")
    else:
        print("Congratulations! You guessed the number.")
    Gcount+=1
    if(Gcount>10 and guess!=num):
        print("Sorry, you should be able to do better.")
        print(f"The number was {num}")
        break
