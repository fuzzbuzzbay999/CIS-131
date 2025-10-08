'''
script: cis131_lab_fractions.py
action: This script is a demonstration of the fraction library.
Author: Declan Juliano
Date:   10/7/2025
'''

# Import Fractions
from fractions import Fraction

# Initialize both fractions
# Any number can be entered in any form, and Fraction will convert it to a fraction
frac1 = Fraction(3.14159265358979323) # A bit of PI
frac2 = Fraction('4/563')             # random numbers

# Print the fractions and their decimal counterparts
print(f'fraction 1 is {frac1} or {float(frac1)}')
print(f'fraction 2 is {frac2} or {float(frac2)}')
print('')

# Add fractons
frac_add=frac1+frac2
print(f'The addition of {frac1} and {frac2} is equal to {frac_add}')

# Subtract fractions
frac_sub=frac1-frac2
print(f'The subtraction of {frac1} and {frac2} is equal to {frac_sub}')

# Multiply fractions
frac_mul= frac2*frac1
print(f'The multiplication of {frac1} and {frac2} is equal to {frac_mul}')

# Print fraction
print(f'To print fractions in a/b, it can be done by printing a variable of Fraction say "frac1", as in {frac1}, or we can print the numerator and denominator seperated by a /, as in {frac1.numerator}/{frac1.denominator}')

# Convert fraction to decimal
print(f'The decimal of {frac1} is {float(frac1)}')

print('')

# Initialize both complex numbers
num1 = complex(2,5)
num2 = complex(3,3.42)

# Complex addition
c_add = num1+num2
print(f'The addition of {num1} and {num2} is equal to {c_add}')

# Complex subtraction
c_sub = num2-num1
print(f'The subtraction of {num1} and {num2} is equal to {c_sub}')

# Getting the real and imaginary parts
print(f'The complex number {num1} consists of the real part: {num1.real} and its imaginary part: {num1.imag}')
