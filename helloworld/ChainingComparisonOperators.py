"""
This module demonstrates chaining Compariosn Operators.
Chaining comparison operators allow you to compare a value against multiple conditions in a single expression.
and is particularly useful for checking if a value falls within a specific range.
We can chain multiple comparison operators together to create more complex conditions.
  
"""

age = 25

if 18 <= age < 65:     # this is what we call chaining comparison operators
    print("Eligible")  # this block will be executed if age is between 18 and 65


"""
Here is a small workout for you to practice changing comparison operators.
1. Create a variable called temperature and assign it a value.
2. Write an if statement that checks if the temperature is between 20 and 30 (inclusive). If true, print "The weather is nice.".
3. Modify the if statement to check if the temperature is NOT between 20 and 30. If true, print "The weather is extreme.".
4. Test your code with different temperature values to see how the output changes.
5. Additionally, create a variable called score and check if it is greater than or equal to 50 and less than 100. Print "Valid score" if the condition is met, otherwise print "Invalid score".
"""
