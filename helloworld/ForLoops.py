"""
This module demonstrates for loops in Python.
A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
It allows you to execute a block of code multiple times, once for each item in the sequence
with comments explaining each part.
or when you know in advance how many times you want to execute a statement or a block of statements.
Or when we want to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
Each example is showcased with print statements to display the output.
"""


for number in range(5):  # using for loop to iterate over a range of numbers from 0 to 4
    print("Attempt", number + 1, (number + 1 ) * "." )  # printing attempt number with dots 


for number in range(1, 20): # using for loop to iterate over a range of numbers from 1 to 19
    if number % 2 == 0:  # checking if the number is even
        print(number)    # printing the even number


for number in range(1, 20): # using for loop to iterate over a range of numbers from 1 to 19        
    print("Attempt", number, number * ".")  # printing attempt number with dots
    if number % 2 == 0:  # checking if the number is even(like 2,4,6,8 etc)
        print("Even number:", number)  # printing the even number


"""Here is a small workout for you to practice for loops.
1. Create a for loop that iterates over the numbers from 1 to 30.
2. Inside the loop, check if the current number is a multiple of 3. If it is, print "Fizz".
3. If the number is a multiple of 5, print "Buzz".
4. If the number is a multiple of both 3 and 5, print "FizzBuzz".
5. If the number is not a multiple of either, simply print the number itself.
Create a variable called total and initialize it to 0.
Use a for loop to iterate over the numbers from 1 to 100.
Creawe a for loop that calculates the sum of all even numbers between 1 and 100.te a variable called total and add each even number to it during the loop.
After the loop, print the value of total to see the sum of all even numbers.
"""
        


