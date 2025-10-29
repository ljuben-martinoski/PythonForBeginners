"""
This module demonstrates comparison operators in Python.
It includes examples of greater than, less than, greater than or equal to, 
less than or equal to, equality, and inequality comparisons.
Each comparison is showcased with comments explaining the expected output.
"""

10 > 3     # This is a greater than comparison  will return  True 
10 < 3     # This is a less than comparison  will return  False
10 >= 3    # This is a greater than or equal to comparison will return  True
10 <= 3    # This is a less than or equal to comparison  will return  False
10 == 3    # This is an equality comparison  will return  False
10 != 3    # This is a not equal to comparison   will return    True
10 == "10" # This compares integer with string, which will return False
"bag" > "apple"  # This compares two strings lexicographically, will return True because 'b' > 'a'
"bag" == "Bag"  # This compares two strings considering case sensitivity, will return False because lowercase 'b' is not equal to uppercase 'B'

## you wuill never use the following in real code, just for demonstration purpose

ord("a") # This returns the Unicode code point of the character 'a', which is 97
ord("b") # This returns the Unicode code point of the character 'b', which is 98    
ord("B") # This returns the Unicode code point of the character 'B', which is 66

"""Here is a small workout for you to practice comparison operators.
1. Create two variables, x and y, and assign them integer values.
2. Use comparison operators to compare these variables in the following ways:
   - Check if x is greater than y.
   - Check if x is less than or equal to y.
   - Check if x is equal to y.
   - Check if x is not equal to y.  
3. Print the results of each comparison to the console.
4. Test your code with different values for x and y to see how the results change.
5. Additionally, compare two string variables and print the results."""