# CIS 131 - assignemnt 2
# Declan Juliano
# Date: 8/22/2025
# This program calculates the min and max target heart rate based on age

age = input("Enter your age in years: ")
max_rate = 220 - int(age)
target_lower = round(max_rate * 0.5)
target_upper = round(max_rate * 0.85)
print("Your maximum heart rate should be", max_rate, "beats per minute")
print("Your target heart rate is between", target_lower, "and", target_upper, "beats per minute")

