"""
For-Else statements in Python are used to execute a block of code based on a condition.
The 'for' part iterates over a sequence (like a list or range), and the 'else' part executes after the loop completes normally (i.e., not terminated by a 'break' statement).
This construct is useful when you want to perform an action after successfully completing a loop without interruptions.
"""

succesfull = False

for number in range(5):  # using for loop to iterate over a range of numbers from 0 to 4
    print("Attempt")
    if succesfull:  # checking if the operation was successful
        print("Successful")  # if condition is true this block will be executed
else:
    print("Attempted 5 times and Failed")  # else block will be executed after the for loop completes normally



