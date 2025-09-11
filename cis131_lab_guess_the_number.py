'''
script: cis131_lab_guess_the_number.py CIS 131 - lab 2
action: This program is a "guess the number" game where the user tries to guess a randomly generated number between 1 and 1000 in 10 tries or less.
Author: Declan Juliano
Date:   8/26/2025, 
        ammended 9/10 (doc strings added) 
'''


from random import randint

#generate the random number
num=int(randint(1,1000))
#initialize variables
guess=0
Gcount=0
maxCount=10
#loop until user guesses the number or exceeds 10 tries
while guess!=num:
    #prod user for a guess
    guess=int(input("Enter your guess between 1 and 1000: "))
    #increment the number of tries
    Gcount+=1
    #if the guess is too low, too high, or correct, give feedback
    if guess<num:
        print(f"Too low, try again, you have {maxCount-Gcount} tries left")
    elif guess>num:
        print(f"Too high, try again, you have {maxCount-Gcount} tries left")
    else:
        #wahoo!!
        print(f"Congratulations! You guessed the number in {Gcount} tries")

    #if tries exceed 10, end the game
    if(Gcount>maxCount and guess!=num):
        print("Sorry, you should be able to do better.")
        print(f"The number was {num}")
        #end the loop due to the fail condition being met and the guess not equaling the number
        break
