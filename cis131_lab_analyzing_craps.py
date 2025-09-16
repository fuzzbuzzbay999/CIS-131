

"""Simulating the dice game Craps."""

import random
def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

#win and lose dictionaries 
wins = {}
lose = {}

#number of games to play
total_games=1000000

#simulate however many total_games is
for roll in range(total_games):
    
    # determine game status and point, based on first roll
    die_values = roll_dice()  # first roll
    sum_of_dice = sum(die_values)
    #first roll so roll = 1
    rolls =1

    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'

    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        sum_of_dice = sum(die_values)
        #increment rolls for this game
        rolls+=1
        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
    
    if game_status == 'WON':
        #if the game is won then increment the dict key for number of rolls needed, if the key doesnt exist, then make it
        wins[rolls] = wins.get(rolls, 0) + 1
    else:
        #if the game is lost then increment the dict key for number of rolls needed, if the key doesn't exist, then make it
        lose[rolls] = lose.get(rolls, 0) + 1
    
#calculate the total wins and lose percentages to the total games played
totalWins = sum(wins.values())
totalLose = sum(lose.values())
print(f"Percentage of wins: {totalWins / total_games * 100:.4f}%")
print(f"Percentage of losses: {totalLose/ total_games * 100:.4f}%\n")

#calculate the percentages of resolved games to the total number of  games with respect to the number of rolls
all_rolls = sorted(set(wins.keys()).union(lose.keys()))
cumulative = 0
print("Roll\t% resolved \tCumulative % \twins \tlosses")
for roll in all_rolls:
    win_count = wins.get(roll, 0)
    loss_count = lose.get(roll, 0)
    total_count = win_count + loss_count
    percent = total_count / total_games * 100
    cumulative += percent
    print(f"{roll}\t{percent:.2f}%\t\t{cumulative:.2f}%\t\t{win_count}\t{loss_count}")