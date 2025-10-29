"""
In progamming we have this cnocept called nested loops.
A nested loop is a loop inside another loop.
The "inner loop" will be executed one time for each iteration of the "outer loop".
This module demonstrates nested loops in Python.
Each example is showcased with print statements to display the output.
They are useful for iterating over multi-dimensional data structures, such as matrices or grids.
"""


for x in range(5):  # outer loop iterating over range of numbers from 0 to 4
    for y in range(3):  # inner loop iterating over range of numbers from 0 to 2
        print(f"({x}, {y})")  # printing the current values of x and y in tuple format

"""Here is a small workout for you to practice nested loops.
1. Create a nested loop where the outer loop iterates over the numbers 1 to 4 (inclusive).
2. The inner loop should iterate over the numbers 1 to 3 (inclusive).   
3. Inside the inner loop, print the product of the current values of the outer and inner loop variables in the format "Outer: x, Inner: y, Product: z".
"""        

