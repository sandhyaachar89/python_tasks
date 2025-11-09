#Q1-Write a Python function named add that takes two arguments a and b and returns their sum.
def add():
    num1 = 10
    num2 = 34
    print(num1+num2)
add()
 
#Q2-Write a Python function named square that takes a number x as input and returns its square.
def square(x):
    return x**2
num = int(input("Enter the number:"))
result = square(num)
print(f"The square of {num} is:{result}")

#Q3-Write a Python function named factorial that takes a positive integer n as input and returns its factorial.
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
num = int(input("Enter the a positive number:"))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

#Q4-Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.
def maximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
nums = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in nums]  
result = maximum(nums)
print("The maximum value in the list is:", result)

#Q5-Write a Python function named reverse that takes a string s as input and returns its reverse.
def reverse():
    char = input("Enter the string:")
    return char[::-1]
obj = print(reverse())
print(obj)


#Q6-Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False .
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
obj = is_prime(10)
print("value:",obj)

#Q7-Write a Python function named fibonacci that takes a positive integer n as input and returns the n th Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


#Q8-Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False .
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # ignore case and spaces
    return s == s[::-1]


#Q9-Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.
def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)


#Q10-Write a Python function named average that takes a list of numbers as input and returns the average value.
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

