"""This script demonstrates the use of conditional statements in Python.
It checks the value of a temperature variable and prints messages based on its value.
It is meant to illustrate if, elif, and else statements. Which are conditional statements used to 
execute different blocks of code based on certain conditions.
With comments explaining each part."""    



temperature = 25         # Example temperature value


if temperature > 30:              # checking if temperature is greater than 30
    print("It's a hot day.")      # if condition is true this block will be executed 
elif temperature < 10:            # checking if temperature is less than 10 , you can add ellif statments as many as you want
    print("It's a cold day.")     # if elif condition is true this block will be executed
else:                          # if none of the above conditions are true this block will be executed
    print("It's a lovely day.")   # else block


"""Here is a small workout for you to practice conditional statements.
1. Create a variable called age and assign it a value.
2. Write an if statement to check if age is less than 18. If true, print "You are a minor.".    
3. Add an elif statement to check if age is between 18 and 65 (inclusive). If true, print "You are an adult.".
4. Add an else statement to print "You are a senior citizen." if age is greater than 65.
5. Test your code with different age values to see the output for each condition.
"""

