"""
This module demonstrates working with numbers in Python.
It includes examples of different numeric types, arithmetic operations,
and usage of the math module for advanced mathematical functions.
Each example is accompanied by print statements to display the output.
"""




x = 1 # this is an integer
y = 2.5 # this is a float
z = x + y # adding integer and float
c = 1 + 2j # this is a complex number, and j is the imaginary unit
print(9 + 9) # addition
print(9-9) # subtraction
print(9*9) # multiplication
print(9/3) # division always results in a float , even if the division is exact if we want integer result we can use floor division
print(9.0/3.0) # division with float numbers which gives float result
print(9//2) # floor division results in an integer, witch means it removes the decimal part and gives only whole number
print(9**2) # exponentiation which is 9 raised to the power of 2
print(9%2) # modulus operator gives the remainder

a = 10
a = a + 3 # incrementing a by 3 which is equivalent to a += 3
a += 3 # shorthand for incrementing a by 3 which is equivalent to a = a + 3

print("===================================================================================================================")
# Working with numbers

print(round(3.6)) # rounding to nearest integer
print(abs(-7.5)) # absolute value   

import math # importing math module for advanced mathematical functions, 
#which provides access to mathematical functions like square root, sine, cosine, etc.
# the following are math module nuber -theoretic and representation functions
print(math.ceil(10.2)) # ceiling function which rounds a number up to the nearest integer
print(math.floor(4.7)) # floor function which rounds a number down to the nearest integer
print(math.sqrt(16)) # square root function which returns the square root of a number
print(math.factorial(5)) # factorial function which returns the factorial of a number
print(math.gcd(48, 18)) # greatest common divisor function which returns the greatest common divisor of two numbers
print(math.sin(math.pi/2)) # sine function which returns the sine of an angle in radians
print(math.cos(0)) # cosine function which returns the cosine of an angle in radians
print(math.log(100, 10)) # logarithm function which returns the logarithm of
# a number to a specified base (base 10 in this case)
print(math.exp(2)) # exponential function which returns e raised to the power of a number   
print(math.pow(2, 3)) # power function which returns a number raised to the power of another number
print(math.radians(180)) # converts degrees to radians
print(math.degrees(math.pi)) # converts radians to degrees
print(math.isqrt(20)) # integer square root function which returns the integer square root of a number
print(math.copysign(3, -2)) # returns a float with the magnitude of the first argument and the sign of the second argument
print(math.hypot(3, 4)) # returns the Euclidean norm, sqrt(x*x + y*y)
print(math.trunc(4.7)) # truncates the decimal part and returns the integer part of a number
print(math.fabs(-5.5)) # returns the absolute value of a float number
print(math.prod([1, 2, 3, 4])) # returns the product of a start value (default: 1) times an iterable of numbers


"""Here is a small workout for you to practice working with numbers.
1. Create two variables, a and b, and assign them the values 15 and 4 respectively.
2. Perform and print the results of the following operations using these variables: addition, subtraction, multiplication, division, floor division, exponentiation, and modulus.
3. Use the math module to calculate and print the square root of a, the factorial of b, and the greatest common divisor (GCD) of a and b.
4. Finally, round the result of a divided by b to the nearest integer and print it.
"""
