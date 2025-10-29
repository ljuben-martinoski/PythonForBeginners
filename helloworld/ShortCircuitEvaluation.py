"""
This module demonstrates short-circuit evaluation in Python.
Short-circuit evaluation means that in logical operations,
the second operand is evaluated only if necessary.
This is particularly useful in preventing errors and optimizing performance.
"""
high_income = True # Example condition indicating high income, boolean value
good_credit = True # Example condition indicating good credit score, boolean value 
student = True   # Example condition indicating if the person is a student, boolean value

if high_income or good_credit and not student:  # using 'or', 'and', and 'not' operators with short-circuit evaluation
    print("Eligible for loan")   # this block will be executed if high_income is True or good_credit is True and student is False
 