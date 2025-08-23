# CIS 131 - assignemnt 2
# Declan Juliano
# Date: 8/22/2025
# This program calculates the min and max target heart rate based on age

age = input("Enter your age in years: ")
max_heart_rate = 220 - int(age)
target_heart_rate_lower = round(max_heart_rate * 0.5)
target_heart_rate_upper = round(max_heart_rate * 0.85)
print("Your maximum heart rate should be", max_heart_rate, "beats per minute")
print("Your target heart rate is between", target_heart_rate_lower, "and", target_heart_rate_upper, "beats per minute")

