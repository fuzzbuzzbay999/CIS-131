from fractions import Fraction

frac1=Fraction('2/4')
frac2 = Fraction('3/100')
frac3=frac1+frac2
print(frac3)

frac3=frac1-frac2
print(frac3)

frac3= frac2*frac1
print(frac3)

print(float(frac3))

num1 = complex(2,5)
num2 = complex(3,3.42)
num3 = num1+num2
print(num3)

num3 = num2-num1
print(num3)

print(num3.real)
print(num3.imag)