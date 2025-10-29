'''
script: cis131_lab_towers.py
action: A recursive function that calculates the solution to Towers of Hanoi with N discs
Date:   10/28/2025
'''

def hanoi(n, source, target, auxiliary):
    # If final disc, move to the target
    if n == 1:
        print(f"{source} → {target}")
    else:
        # move the next disc from the source to the auxiliary peg using the target peg as a stash
        hanoi(n - 1, source, auxiliary, target)
        # print the movement
        print(f"{source} → {target}")
        # move the same disc to the target using the source peg as a stash
        hanoi(n - 1, auxiliary, target, source)

# Move 64 disks from peg 1 to peg 3
num_disks = 64
hanoi(num_disks, 1, 3, 2)
