"""
This module demonstrates type conversion in Python.
It includes an example of converting user input from string to integer.
"""


x = input("x: ") # we use input to get input from the user 
a = int(x) + 10 # here x is string so we need to convert it to integer
#int(x)
#float(x)
#bool(x)
#str(x)
print(f" x: {x} a: {a}")


"""Here is a small workouts for you to practice type conversion.
1. Get a number from the user using input() and store it in a variable.
2. Convert the input to a float and store it in another variable.
3. Multiply the float value by 2.5 and store the result in a third variable.
4. Print the original input, the float value, and the result of the multiplication using an f-string."""