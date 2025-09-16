import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

# Track wins and losses by number of rolls
wins = {}
losses = {}

total_games = 1_000_000

for _ in range(total_games):
    rolls = 1
    die1, die2 = roll_dice()
    sum_dice = die1 + die2

    if sum_dice in (7, 11):
        result = 'WON'
    elif sum_dice in (2, 3, 12):
        result = 'LOST'
    else:
        point = sum_dice
        result = 'CONTINUE'

        while result == 'CONTINUE':
            die1, die2 = roll_dice()
            sum_dice = die1 + die2
            rolls += 1

            if sum_dice == point:
                result = 'WON'
            elif sum_dice == 7:
                result = 'LOST'

    # Update dictionaries
    if result == 'WON':
        wins[rolls] = wins.get(rolls, 0) + 1
    else:
        losses[rolls] = losses.get(rolls, 0) + 1

# Calculate totals
total_wins = sum(wins.values())
total_losses = sum(losses.values())

print(f"Percentage of wins: {total_wins / total_games * 100:.1f}%")
print(f"Percentage of losses: {total_losses / total_games * 100:.1f}%\n")

print("Roll\tWin/Loss %\tCumulative %")

# Combine all roll counts
all_rolls = sorted(set(wins.keys()).union(losses.keys()))
cumulative = 0

for roll in all_rolls:
    win_count = wins.get(roll, 0)
    loss_count = losses.get(roll, 0)
    total_count = win_count + loss_count
    percent = total_count / total_games * 100
    cumulative += percent
    print(f"{roll}\t{percent:.2f}%\t\t{cumulative:.2f}%")
