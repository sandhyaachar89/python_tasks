#operators task
#addition
num_1 = 25
num_2 = 65
result = num_1 + num_2
print(result)

#subtraction
num_1 = 78
num_2 = 43
result = num_1 - num_2
print(result)

#multiplication
num_1 = 78
num_2 = 98
result = num_1 * num_2
print(result)

#exponent
num_1 = 7
num_2 = 4
result = num_1 ** num_2
print(result)

#division
num_1 = 4
num_2 = 86
result = num_1 / num_2
print(result)

#modulus
num_1 = 5
num_2 = 225
result = num_1 % num_2
print(result)

#comparition 
num_1 = 56
num_1 += 5
print(num_1)
num_1 = 87
num_2 = 117
print(num_1==num_2)
print(num_1!=num_2)
print(num_1>num_2)
print(num_1<num_2)
print(num_1>=num_2)
print(num_1<=num_2)

#task
#Q1-Write a Python program to calculate the area of a rectangle using the given formula: area = length * width . Take the values of length and width as inputs from the user.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area}")

#Q2-Write a Python program to demonstrate incrementing and decrementing a variable
number = 10
print(f"Initial value: {number}")
number += 1
print(f"After incrementing by 1: {number}")
number -= 1
print(f"After decrementing by 1: {number}")
number += 5
print(f"After incrementing by 5: {number}")
number -= 3
print(f"After decrementing by 3: {number}")

#Q3-Write a Python program to convert temperature from Celsius to Fahrenheit. The formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

#Q4-Write a Python program to calculate the simple interest given the principal amount, rate, and time (in years).
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")

#Q5-Write a Python program to concatenate two strings and display the result. The strings should be taken as input from the user.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = string1 + string2
print(f"The concatenated string is: {result}")

#Q6-Write a Python program to convert a distance from kilometers to miles.
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles} miles")