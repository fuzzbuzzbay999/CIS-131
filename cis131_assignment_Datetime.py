
'''
script: cis131_lab_Datetime.py
action: This script is a demonstration of the datetime library
Author: Declan Juliano
Date:   10/7/2025
'''

# Import datetime
from datetime import datetime

# Get the current date and time and store it to x and y
x = datetime.now()
y = datetime.now()

# Display each datetime object
print("Datetime object x:", x)
print("Datetime object y:", y)

# Display each datetime object’s data attributes individually
print("\nAttributes of x:")
print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)
print("Hour:", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)
print("Microsecond:", x.microsecond)

print("\nAttributes of y:")
print("Year:", y.year)
print("Month:", y.month)
print("Day:", y.day)
print("Hour:", y.hour)
print("Minute:", y.minute)
print("Second:", y.second)
print("Microsecond:", y.microsecond)

# Use comparison operators to compare the two datetime objects
print("\nComparison Results:")
print("x == y:", x == y)
print("x < y:", x < y)
print("x > y:", x > y)

# Calculate the difference between y and x
difference = y - x
print("\nDifference between y and x:", difference)
print("Total seconds difference:", difference.total_seconds())