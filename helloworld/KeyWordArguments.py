"""
Here we will look into keyword arguments in Python functions.
Keyword arguments allow you to specify arguments by the parameter name,
making your function calls more explicit and easier to read.
This is especially useful when a function has many parameters, or when some parameters have default values.
"""


def incremnet(number, by): # defining a function with two parameters: number and by
    return number + by # returning the sum of number and by


result = incremnet(2, by=1)  # positional arguments
print(result)  # Output: 3


""""
Here in this code by= is the keyword argument.
We are explicitly specifying that the value 1 is for the parameter by.  
Which makes the code more readable and clear.
We can also use keyword arguments for all parameters."""