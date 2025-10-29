"""
This module demonstrates While Loops in Python.
A while loop repeatedly executes a block of code as long as a specified condition is true.
It is useful when the number of iterations is not known in advance
or when you want to continue looping until a certain condition changes.
Each example is showcased with print statements to display the output
and comments explaining each part.
With a small workout at the end for practice.
"""


number = 100 
while number > 0:  # while loop that continues as long as number is greater than or equal to 0
    print(number)   # printing the current value of number
    number = number // 2  # updating number by performing integer division by 2

""""
Under you have a code for the command line echo program using while loop.
withc can be used to echo user input until the user types "quit" to exit the program.
It must be doen in a terminal or command prompt that supports input function.
"""
command = ""  # initializing command variable with an empty string   
while command != "quit":  # while loop that continues until command is equal to "quit"
    command = input(">")   # getting user input and storing it in command variable
    print("ECHO", command)  # printing the echo of the command entered by the user

    