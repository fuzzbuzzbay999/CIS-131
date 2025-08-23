# CIS 131 - assignment 1
# Declan Juliano
# Date: 8/22/2025
# This program calculates the value of an investment over a period of time


#initiate the variables
n = 1000  # Initial investment amount
t = (10,20,30) # Tuple of years to calculate investment value
r = 7 # Interest rate in percentage

# Function to calculate the investment value
def investment_value(n, r, t):
    r = r / 100  # Convert percentage to decimal
    return round((n * (1 + r) ** t),2) #do the math and round to 2 decimal places

print("if you invest $1000 at 7% interest you will have:") #output statement
#iterate through the tuple t and print the investment value for each year
for i in t: 
    print("at",i,"years $",investment_value(1000, r, i))

# CIS 131 - Homework 1
# Declan Juliano
# Date: 8/22/2025
# This program calculates the value of an investment over a period of time


#initiate the variables
n = 1000  # Initial investment amount
t = (10,20,30) # Tuple of years to calculate investment value
r = 7 # Interest rate in percentage

# Function to calculate the investment value
def investment_value(n, r, t):
    r = r / 100  # Convert percentage to decimal
    return round((n * (1 + r) ** t),2) #do the math and round to 2 decimal places

print("if you invest $1000 at 7% interest you will have:") #output statement
#iterate through the tuple t and print the investment value for each year
for i in t: 
    print("at",i,"years $",investment_value(1000, r, i))
