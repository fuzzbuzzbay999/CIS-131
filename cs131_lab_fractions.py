'''
script: cis131_lab_fractions.py
action: This script is a demonstration of the fraction library.
Author: Declan Juliano
Date:   10/7/2025
'''

# Import Fractions
from fractions import Fraction

# Initialize both fractions
frac1=Fraction('2/4')
frac2 = Fraction('3/100')

# Add fractons
frac_add=frac1+frac2
print(f'The addition of {frac1} and {frac2} is equal to {frac1+frac2}')

# Subtract fractions
frac_sub=frac1-frac2
print(f'The subtraction of {frac1} and {frac2} is equal to {frac1-frac2}')

# Multiply fractions
frac_mul= frac2*frac1
print(f'The multiplication of {frac1} and {frac2} is equal to {frac1*frac2}')

# Print fraction
print(f'To print fractions in a/b, it can be done by printing a variable of Fraction like frac1, as in {frac1}, or we can print the numerator and denomerator seperated by a /, as in {frac1.numerator}/{frac1.denominator}')

# Convert fraction to decimal
print(f'The decimal of {frac2} is {float(frac2)}')

print('')

# Initialize both complex numbers
num1 = complex(2,5)
num2 = complex(3,3.42)

# Complex addition
c_add = num1+num2
print(f'The addition of {num1} and {num2} is equal to {num1+num2}')

# Complex subtraction
c_sub = num2-num1
print(f'The subtraction of {num1} and {num2} is equal to {num1-num2}')

# Getting the real and imaginary parts
print(f'the complex number {num1} consists of the real part: {num1.real} and its imaginary part: {num1.imag}')
