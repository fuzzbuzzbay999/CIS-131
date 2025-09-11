'''
script: cis131_lab_miles_per_gallon.py CIS 131 - lab 1
action: This program calculates the average miles per gallon for multiple trips
Author: Declan Juliano
Date:   8/22/2025, 
        ammended 9/10 (doc strings added and faulty logic fixed) 
'''

#initiate the variables
isRunning = True
totalMiles = 0
totalGallons = 0
Ampg = 0

# Loop to get user input and calculate miles per gallon
while(isRunning):
    #prompt user for input
    gallons = float(input("Enter number of gallons used (-1 to end): "))
    #if sentinel value is entered, exit the loop
    if gallons == -1:
        #set isRunning to False to prevent any undeeded errors if this script gets used for anything else.
        isRunning = False
        #exit the loop and proceed
        break
    #prompt user for miles driven
    miles = float(input("Enter number of miles driven: "))
    #calculate miles per gallon and print the result
    mpg = miles / gallons 
    print(f"The miles/gallon for this tank was {mpg:.6f}")
    #add the miles and gallons to the running total
    totalMiles += miles
    totalGallons += gallons


#after exiting the loop, calculate the average mpg aslong as both are greater than zero. (so no divide by zero error happens) if the loop is imediately terminated
if(totalMiles>0 and totalGallons>0): 
    Ampg=totalMiles/totalGallons
    # print the average miles per gallon
    print(f"The overall average miles/gallon was: {Ampg:.6f}")
