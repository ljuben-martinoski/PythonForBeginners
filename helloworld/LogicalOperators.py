"""
We use logical operators to model complex conditions by combining multiple boolean expressions.
This module demonstrates the use of logical operators: and, or, and not.    

The 'and' operator returns True if both operands are True.
The 'or' operator returns True if at least one operand is True. 
The 'not' operator negates the boolean value of its operand.
Each example is showcased with comments explaining the expected output.
    """

high_income = True    # Example condition indicating high income, boolean value
good_credit = False   # Example condition indicating good credit score, boolean value
student = True      # Example condition indicating if the person is a student, boolean value


if high_income and good_credit:   # using 'and' operator to check if both conditions are true
    print("Eligible for loan")    # this block will be executed only if both conditions are true
else:
    print("Not eligible for loan") # this block will be executed if any of the conditions is false

if not student:               # using 'not' operator to negate the student condition
    print("Eligible for non-student loan")  # this block will be executed if student is False
else:
    print("Not eligible for student loan")      # this block will be executed if student is True
         


"""Here is a small workout for you to practice logical operators.
1. Create three boolean variables: is_raining, has_umbrella, and is_windy.
2. Write an if statement that uses the 'and' operator to check if it is raining and the person has an umbrella. If both conditions are true, print "You can go outside.".
3. Write another if statement that uses the 'or' operator to check if it is not raining or the person has an umbrella. If either condition is true, print "You can go outside.".
4. Finally, use the 'not' operator to check if it is not windy. If it is not windy, print "It's a calm day.".
5. Test your code with different values for the boolean variables to see how the output changes.
"""