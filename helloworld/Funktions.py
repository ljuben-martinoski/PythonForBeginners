"""
This module demostrates the Functions in Python.
A function is a reusable block of code that performs a specific task.
Functions help in organizing code, improving readability, and reducing redundancy.
They can take inputs (parameters) and return outputs (return values).
Each example is showcased with print statements to display the output
and comments explaining each part.
They are useful for breaking down complex problems into smaller, manageable pieces. 
Especialy when writing large programs.
"""
# this 3 are build funktions in python as for many more
# print()   using the built-in print function to display output to the console
# round()   using the built-in round function to round a floating-point number to the nearest integer
# sum()     using the built-in sum function to calculate the sum of a list of numbers


""" now we are going to learn how to write our own funktions, it is useful when you are writnig a 
 lot of code and then braking it into more smaller maintainable and potentialy more reusable chunks of code.
 Let me show you how we can write our own funktions in python.
 We start with defining a funktions using the def keyword followed by the funktions name(giving a name) and parentheses."""

#use small words to name your funktions and underscores to separate words if needed.kepp it nice and simple.


def greet(): # by doing so giving () and : we are sainig thea to the following def we are givnig funktions
    print("hi there")
    print("welcome aboard")

# now we have defined a funktions called greet that prints a welcome message when called.
# to execute the funktions we need to call it by its name followed by parentheses.
greet()

"""
Defining  Funktions
the difference bretween def  and the funktion greet() is that the greet() funktion dosent take inputs or parameters.
on the other hand def takes inputs or parameters to make the funktion more flexible and reusable.
when we asre definni a funktion we create parameters within the parentheses()
"""          
def greet(first_name, last_name): # here first_name and last_name are parameters
    print("hi ther")
    print("welcome aboard")
  
greet("Mosh", "Hamedani") # here "Mosh" and "Hamedani" are arguments passed to the parameters,when we are calling the funktion. 
#so aktualy greet() here is the calling the funktion with the arguments "Mosh" and "Hamedani".
greet("Jane", "Doe")


"""Just to be clear the Parametars is the input that youndefine for your funktion.
Wheras an argument is the actula value for a given parameter."""

"""Types of Funktions
1. Funktions that perform a task.
2. Funktions that calculate and return a value."""

def greet(name):
    print(f"hi {name}")# lets show how to return a value from a funktion, because here we are just printing a message.


def get_greeting(name):
    return f"hi {name}" # here we are using the return statement to send back a value from the funktion.

message = get_greeting("Mosh") # here we are calling the funktion and storing the returned value in a variable called message.
file = open("content.txt", "w") # here we are opening a file in write mode.
file.write(message) # here we are writing the message to the file.


