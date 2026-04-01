#Q1-Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of each number in the input list. Use the map() function with a lambda function to implement this.
def square_all(numbers):
    return list(map(lambda x: x**2, numbers))
nums = [1, 2, 3, 4, 5]
print(square_all(nums)) 



#Q2-Write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. Use the filter() function with a lambda function to implement this. Write a Python function
def filter_positive(numbers):
    return list(filter(lambda x: x > 0, numbers))
nums = [-5, 3, 0, -2, 8, 7, -1]
print(filter_positive(nums))



#Q3-calculate_factorial(n) that calculates the factorial of a given number n. Use the reduce() function with an appropriate lambda function to implement this.
from functools import reduce
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(calculate_factorial(5))   # Output: 120
print(calculate_factorial(0))

#Q4-Write a Python function count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce() function with an appropriate lambda function to implement this.
from functools import reduce
def count_vowels(string):
    vowels = "aeiouAEIOU"
    return reduce(lambda count, ch: count + (1 if ch in vowels else 0), string, 0)
print(count_vowels("Hello World"))     
print(count_vowels("PYTHON"))         
print(count_vowels("Beautiful Day"))