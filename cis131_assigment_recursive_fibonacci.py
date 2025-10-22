'''
script: cis131_assignment_recursive_power_function.py
action: a function that recursivly calculates a fibonacci number at an index of the series stating at 0
Author: Declan Juliano
Date:   10/21/2025
'''

# Function fibonacci 
def fibonacci(n):
    # Increment the global count variable everytime this function is called
    global Count
    Count +=1
    # Calculated a fibonacci number at n
    if n in (0, 1):  # base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to count and call fibonacci
def Count_fibonacci(n):
    # Reset the global count variable
    global Count
    Count = 0
    # Calculate the fibonacci number at n and store in ans
    ans = fibonacci(n)
    # Print the number and amount of itterations
    print(f"The fibnacci number at index {n} is {ans} with {Count} function calls")

# Test calls
Count_fibonacci(10)

Count_fibonacci(20)

Count_fibonacci(30)