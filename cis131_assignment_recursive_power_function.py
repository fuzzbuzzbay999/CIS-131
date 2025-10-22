'''
script: cis131_assignment_recursive_power_function.py
action: a function that recursivly calculates a number to a power
Author: Declan Juliano
Date:   10/20/2025
'''

# power function
def power(base, exponent):
    # If the exponent is 0 then return 1 
    if exponent == 0:
        return 1
    else:
        # Rerun the function with exponent - 1
        return base * power(base, exponent - 1)


print(power(3, 4))  # Calculate and print 3^4
