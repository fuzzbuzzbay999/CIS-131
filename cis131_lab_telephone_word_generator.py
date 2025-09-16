
from itertools import product
#no q or z
#dict of numbers and their associated letters
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
isRunning = True

while (isRunning):
    #prompt user for a phone number or -1 to end
    teleNum = input("Please input your desired telephone number in the format xxx-xxxx (-1 top stop): ")
    #if sentenial value then stop imediately 
    if(teleNum == '-1'):
        isRunning = False
        break

    #iterate through teleNum, and add all digits to teleIntOnly
    teleIntOnly = ""
    for i in teleNum:  
        if(i.isdigit()):
            teleIntOnly+=(i)

    print("All letter combinations for " + teleIntOnly)

    #if the length of teleIntOnly is 7 proceed:
    if(len(teleIntOnly)==7):

        # Get the list of possible letters for each digit
        letter_groups = [numpad[digit] for digit in teleIntOnly]
        
        # Generate Cartesian product of all letter groups
        combinations = [''.join(combo) for combo in product(*letter_groups)]
        
        #print the combinations in rows of 15
        PrevIndex=0
        for i in range(15,len(combinations),15):
            print(combinations[PrevIndex:i])
            PrevIndex=i
        #print the remaining combinations
        print(combinations[PrevIndex:len(combinations)])

    #if the legnth of teleIntOnly was not seven print the reason and loop back to the top to ask again
    else:
        print("the number must be 7 digits")
        print("try again")