course = "Python Programming"
"""
This module demonstrates various string methods in Python.
It includes examples of converting case, stripping whitespace,
finding substrings, and replacing parts of a string.
Each method is showcased with a print statement to display its output.
And comments explaining each part.For each method used in this script.
"""

print(course.upper())  # Convert to uppercase
print(course.lower())  # Convert to lowercase   
print(course.title()) # Convert to title case
print(course.rstrip()) # Remove trailing whitespace
print(course.find("Pro")) # Find substring index
print(course.replace("Python", "Java")) # Replace substring
print("pro" in course) # Check substring presence (case-sensitive)
print("Pro" in course) # Check substring presence (case-sensitive)
print(  course.startswith("Python") ) # Check if string starts with a substring
print(  course.endswith("Programming"))  # Check if string ends with a substring
print(  course.count("o") ) # Count occurrences of a substring  
print(  course.index("P") ) # Get index of first occurrence of a substring
print(  course.isalnum() ) # Check if all characters are alphanumeric   
print(  course.isalpha() ) # Check if all characters are alphabetic 
print(  course.strip() ) # Remove leading and trailing whitespace
print(  course.split() ) # Split string into a list of substrings based on whitespace
print(  course.capitalize() ) # Capitalize the first character of the string
print(  course.center(30) ) # Center the string within a specified width
print(  course.zfill(30) ) # Pad the string on the left with zeros to fill a specified width
print(  course.swapcase() ) # Swap the case of each character in the string
print(  course.partition(" ")) # Partition the string into a tuple around the first occurrence of a substring
print(  course.encode() ) # Encode the string into bytes using default encoding (UTF-8)
print(  course.expandtabs(tabsize=4) ) # Replace tab characters with spaces, using a specified tab size
print(  course.ljust(30) ) # Left-justify the string within a specified width
print(  course.rjust(30) ) # Right-justify the string within a specified width
print(  course.rpartition(" ")) # Partition the string into a tuple around the last occurrence of a substring
print(  course.zfill(50) ) # Pad the string on the left with zeros to fill a specified width of 50  
print(  course.islower() ) # Check if all characters in the string are lowercase
print(  course.isupper() ) # Check if all characters in the string are uppercase
print(  course.istitle() ) # Check if the string is in title case
print(  course.endswith("ing"))  # Check if string ends with a substring "ing"
print(  course.startswith("Java") ) # Check if string starts with a substring "Java"
print(  course.split(" ") ) # Split string into a list of substrings based on space character


"""Here is a small workout for you to practice string methods.
1. Create a string variable with the value "  Hello, Python World!.
2. Use a string method to remove the leading and trailing whitespace.
3. Convert the string to uppercase.
4. Check if the string starts with "HELLO". 
5. Replace "Python" with "Java".
6. Print the final modified string.
7. Print the results of each operation to the console.
"""