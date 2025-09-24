
'''
script: cis131_lab_analyzing_craps.py
action: This script is a craps simulation. It will simulate "total_games" games, and compile the data, per the amount of rolls to complete a game, and the coresponding wins and losses.
Author: Declan Juliano
Date:   9/16/2025
'''

import random
#Win and lose dictionaries 
wins = {}
lose = {}

#Number of games to play
"""change this to change how many games to simulate"""
total_games = 1000000

#Method to roll both dice, then return a tuple
def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  #Pack die face values into a tuple

#Simulate however many total_games is
for roll in range(total_games):
    
    #Determine game status and point, based on first roll
    die_values = roll_dice()    # first roll and set roll = 1
    sum_of_dice = sum(die_values)
    rolls = 1

    #Determine status of the first roll
    if sum_of_dice in (7, 11):  #Win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  #Remember point, continue on
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    #Continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        sum_of_dice = sum(die_values)
        #Increment rolls for this game
        rolls+=1

        #Did the dice win or lose 
        if sum_of_dice == my_point:  #Win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  #Lose by rolling 7
            game_status = 'LOST'

    if game_status == 'WON':
        #If the game is won then increment the dict key in wins for number of rolls needed, if the key doesnt exist, then make it
        wins[rolls] = wins.get(rolls, 0) + 1
    else:
        #If the game is lost then increment the dict key in lose for number of rolls needed, if the key doesn't exist, then make it
        lose[rolls] = lose.get(rolls, 0) + 1
    
#Calculate the total wins and lose percentages to the total games played
totalWins = sum(wins.values())
totalLose = sum(lose.values())
print(f"Percentage of wins: {totalWins / total_games * 100:.3f}%")
print(f"Percentage of losses: {totalLose / total_games * 100:.3f}%\n")

#Calculate the percentages of resolved games to the total number of  games with respect to the number of rolls
all_rolls = sorted(set(wins.keys()).union(lose.keys()))
cumulative = 0
print("Roll\t% resolved \tCumulative % \twins \tlosses")
for roll in all_rolls:
    #Calculate the total win and loss aswell as the total amount of finished games per roll
    win_count = wins.get(roll, 0)
    loss_count = lose.get(roll, 0)
    total_count = win_count + loss_count
    #Calculate the percent of resolved games to the total  games played
    percent = total_count / total_games * 100
    #Add to the cumulative percentile
    cumulative += percent
    #Display: the roll, percent finished, cumulative percent, num of wins, num of losses
    print(f"{roll}\t{percent:.2f}%\t\t{cumulative:.2f}%\t\t{win_count}\t{loss_count}")