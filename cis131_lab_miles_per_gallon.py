# CIS 131 - lab 1
# Declan Juliano
# Date: 8/22/2025
# This program calculates the average miles per gallon for multiple trips

#initiate the variables
isRunning = True
Ampg = 0

# Loop to get user input and calculate miles per gallon
while(isRunning):
    #prompt user for input
    gallons = float(input("Enter number of gallons used (-1 to end): "))
    #if sentinel value is entered, exit the loop
    if gallons == -1:
        isRunning = False
        break
    #prompt user for miles driven
    miles = float(input("Enter number of miles driven: "))
    #calculate miles per gallon and print the result
    mpg = miles / gallons 
    print("The miles/gallon for this tank was", round(mpg,6))
    #calculate the overall average mpg
    Ampg = (Ampg + mpg) / 2  if Ampg != 0 else mpg 

#after exiting the loop, print the overall average mpg
if(not isRunning):
    print("The overall average miles/gallon was", round(Ampg,6))
