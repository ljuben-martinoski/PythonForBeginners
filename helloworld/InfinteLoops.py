"""
This module demostrates and explains the Infinite Loops in Python.
An infinite loop is a loop that continues to execute indefinitely
because the loop's terminating condition is never met.
Infinite loops can occur unintentionally due to programming errors,
or they can be used intentionally in scenarios where continuous operation is required,
such as in servers or real-time systems.
Caution should be exercised when using infinite loops, as they can lead to unresponsive programs or high resource consumption
if not managed properly.
"""
# Example of an infinite loop using while
command = ""  # initializing command variable with an empty string
while command.lower() != "quit":  # while loop that continues until command is equal to "quit" (case insensitive)
    command = input(">")   # getting user input and storing it in command variable
    
    print("ECHO", command)
    break  # printing the echo of the command entered by the user
# Note: To exit the loop, type "quit" (case insensitive) in the input prompt(terminal or command prompt).
# Caution: Be careful when running infinite loops, as they can make your program unresponsive.
# To stop an infinite loop, you can usually use Ctrl + C in the terminal or command prompt.


