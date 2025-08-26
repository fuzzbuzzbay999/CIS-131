3# cis131_lab_guess_the_number.py CIS 131 - lab 2
# Declan Juliano
# Date: 8/26/2025
# This program is a "guess the number" game where the user tries to guess a randomly generated number between 1 and 1000 in 10 tries or less.

from random import randint
#generate random number
num=int(randint(1,1000))
#initialize variables
guess=0
Gcount=0
#loop until user guesses the number or exceeds 10 tries
while guess!=num:
    #prod user for a guess
    guess=int(input("Enter your guess between 1 and 1000: "))
    #if the guess is too low, too high, or correct, give feedback
    if guess<num:
        print("Too low, try again")
    elif guess>num:
        print("Too high, try again")
    else:
        #wahoo!!
        print("Congratulations! You guessed the number.")
    #increment the number of tries
    Gcount+=1
    #if tries exceed 10, end the game
    if(Gcount>10 and guess!=num):
        print("Sorry, you should be able to do better.")
        print(f"The number was {num}")
        #end the loop 
        break
