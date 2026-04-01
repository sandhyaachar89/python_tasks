#loop_task
#Q1-Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop.
sum_of_squares = 0
for i in range(1, 6):
    sum_of_squares += i ** 2  
print("The sum of squares from 1 to 5 is:", sum_of_squares)

#Q2-Write a Python program that uses a while loop to print a countdown from 5 to 1.
count = 5
while count >= 1:
    print(count)
    count -= 1  

#Q3-Write a Python program to print the multiplication table for a user-specified number using a nested for loop.
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    for j in range(1, 2): 
        print(f"{num} x {i} = {num * i}")
    
#Q4-Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive).
sum_even = 0
for i in range(0, 11):
    if i % 2 == 0:  
        sum_even += i
print("The sum of all even numbers between 0 and 10 is:", sum_even)    

#Q5-Calculate the sum of all numbers from 1 to a given number
num = int(input("Enter a number: "))
total = 0
for i in range(1, num + 1):
    total += i
print("The sum of all numbers from 1 to", num, "is:", total)

#Q6-Display numbers from a list using loop
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)

#Q7-Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i)

#Q8-Write a Python program to print the cube of all numbers from 1 to a given number
num=[1,2,3,4,5,6,7,8,9]
for i in num:
    cube=i**3
    print(f"cube of {i} is {cube}")
 


