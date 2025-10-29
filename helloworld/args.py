"""creating a funktion that takes a variable number of arguments
using *args syntax. This allows us to pass a variable number of positional arguments to the function.
The function will sum all the arguments passed to it and return the total.
"""

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

    

print(multiply(2, 3, 4, 5))

(2, 3, 4, 5) # this is tuple