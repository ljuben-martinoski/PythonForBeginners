"""

This module demonstrates the use of strings and variables in Python.
It includes examples of string concatenation, indexing, slicing,
and formatted strings (f-strings).
Each example is accompanied by print statements to display the output."""



x = 2
w = 5
y = x +  w
print("The sum of", x, "and", w, "is", y)
print("HelloWorld")

name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)


course = "Python Programming"
print(len(course) )
# this is comment
# \" to print double quote         
#\'  to print double quote or single quote
# \\  when we want to print a backslash 
# \n new line
# \t tab space  
print(course[0])  # first character
print(course[0:6])  # first 6 characters        
print("HelloWorld") 

full = f"{greeting} Welcome to {course}." # this is an f-string and used to format strings
print(full)

first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}" # Using f-string to concatenate first and last name
print(full_name)


"""Here is a small workout for you to practice strings and variables.
1. Create two string variables, first_name and last_name, and assign them your first and last names.
2. Use an f-string to create a new variable full_name that combines first_name and last_name with a space in between.
3. Print the full_name variable to the console.
4. Create a variable greeting that uses an f-string to say "Hello, [full_name]!".
5. Print the greeting variable to the console.
"""
