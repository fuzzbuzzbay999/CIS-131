'''
script: cis131_lab_guess_the_number.py CIS 131 - lab 2
action: This script generates words that translate to a phonenumber. Input a desired phone number and it will output all possible corresponding letter combinations minus q and z.
Author: Declan Juliano
Date:   9/16/2025
'''

#import product to calculate the cartiesian product. I was unsucessful in using forloops and other methods (trinary counter).
from itertools import product

#Dict of numbers and their associated letters, 0 and 1 are to absorb issues if 1 or 0 are entered bellow
numpad ={
    '0': [' ',' ',' '],
    '1': [' ',' ',' '],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y']

}

#Start
isRunning = True

while (isRunning):
    #Prompt user for a phone number or -1 to end
    teleNum = input("Please input your desired telephone number in the format xxx-xxxx (-1 top stop): ")
    #if sentinel value update isRunning and stop imediately
    if(teleNum == '-1'):
        isRunning = False
        break

    #Iterate through teleNum, and add all digits to teleIntOnly (filtering the input)
    teleIntOnly = ""
    for i in teleNum:  
        if(i.isdigit()):
            teleIntOnly+=(i)

    print("All letter combinations for " + teleIntOnly)

    #If the length of teleIntOnly is 7 proceed:
    if(len(teleIntOnly)==7):

        #Get the list of possible letters for each digit
        letter_groups = [numpad[digit] for digit in teleIntOnly]
        
        #Generate Cartesian product of all letter groups
        combinations = [''.join(combo) for combo in product(*letter_groups)]
        
        #Print the combinations in rows of 15
        PrevIndex=0
        for i in range(15,len(combinations),15):
            print(combinations[PrevIndex:i])
            PrevIndex=i
        #Print the remaining combinations
        print(combinations[PrevIndex:len(combinations)])

    #If the legnth of teleIntOnly was not seven print the reason and loop back to the top, to ask again
    else:
        print("the number must be 7 digits")
        print("try again")