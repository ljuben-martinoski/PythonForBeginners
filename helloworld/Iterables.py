"""
This module will demostrate Iterables in Python.
An iterable is an object that can be iterated (looped) over.    
In Python, common iterable types include lists, tuples, strings, and dictionaries.
Each example is showcased with print statements to display the output.
They are very useful when you want to perform operations on each item in a collection of items.
"""


print(type(6))   # int is not an iterable
print(type(5.5)) # float is not an iterable
print(type(range(5)))  # range is an iterable which means we can iterate over it using loops

for x in ("Python"): 
    print(x)  # iterating over each character in the string "Python"


for x in [1, 2, 3, 4, 5]: # this is a list which is an iterable 
    print(x)  # iterating over each element in the list [1, 2, 3, 4, 5]

shopping_cart = ["apple", "banana", "orange", "mango", "Kiwi", "Pomelo"] # this is a list which is an iterable

for item in shopping_cart: # this is a for loop to iterate over the list shopping_cart
    print(item)  # iterating over each element in the list shopping_cart


"""Here is a small workout for you to practice iterables.
1. Create a list called fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".
2. Use a for loop to iterate over the fruits list and print each fruit in uppercase letters.
3. Create a string variable called word and assign it the value "iteration".#
4. Use a for loop to iterate over each character in the word string and print the character along with its index position in the format "Index: x, Character: y".
5. Create a range of numbers from 1 to 10 using the range() function.
6. Use a for loop to iterate over this range and print only the even numbers.
7. Finally, create a list of your favorite colors and use a for loop to print each color with a message saying "I like [color]".
"""


    













