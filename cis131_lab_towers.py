'''
script: cis131_lab_towers.py
action: A recursive function that calculates the solution to Towers of Hanoi with N discs
Date:   10/28/2025
'''

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"{source} → {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"{source} → {target}")
        hanoi(n - 1, auxiliary, target, source)

# Move 64 disks from peg 1 to peg 3
num_disks = 64
hanoi(num_disks, 1, 3, 2)
