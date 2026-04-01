#Day-2:fundamental_task#
#Q1- Create a Python script with both single-line and multi-line comments explaining the purpose of the script.
# This is a simple Python script to perform addition 

number_1 = 100
number_2 = 148
total_amt = number_1 + number_2
print(total_amt)

"""The above python code is to perform addition
1. value 100 is assigned to variable number_1
2. value 148 is assigned to variable number_2
3. preformed an addition operation using (+) operator and stored the values of number_1 and number_2 in total_amt 
4. printed the total_amt value using print statement"""

#Q2- Declare two variables, one storing an integer and the other a string. Print their values.
item_name = "apple"
print(item_name)
item_no = 456
print(item_no)

#Q3- Write a program that prints a pattern using multiple print statements.
print("      *      ")
print("     * *     ")
print("   * * * *   ")
print(" * * * * * * ")

#Q4- Create a Python script for a simple task and add comments to explain each step.
user_name = (input("enter your name:"))   #take input from the user 
print("Hello, "+user_name+"")              #print the result

#Q5- Create variables of different data types(int,float,str) and print their values.
age = 25  # int type
height = 5.8  # float type
name = "Sandhya" #string type
print("Name:", name)
print("Age:", age)
print("Height:", height)

#Q6- Determine the data type of a variable
age = 37
print(age)
print(type(age))
height = 5.4
print(height)
print(type(height))

#Q7- Display the memory addresses
item_price = 589
print(id(item_price))
item_name = "mango"
print(id(item_name))

#Q8- Create a program that takes user age = “35”, converts it to an integer, and then prints the result type. 
age = "35"  
age_int = int(age)
print("Age after conversion:", age_int)
print("Data type after conversion:", type(age_int))

#Q9- Concatenate two strings and print the result
first_name = "Sandhya"
last_name = "S"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

#task-6

#data types 
a = 10             # int
b = 3.14           # float
c = "Hello"        # str
d = True           # bool
e = [1, 2, 3]      # list
f = (4, 5, 6)      # tuple
g = {"x", "y", "z"}  # set
h = {"name": "Sandhya", "age": 25}  # dict
i = None           # NoneType
 
#type conversion 

#int to float
item_price = 2500
print(item_price)
print(type(item_price))
float_conversion =float(item_price)
print(float_conversion)
print(type(float_conversion))

#float to int
pi_value = 3.14159
print(pi_value)
print(type(pi_value))
int_conversion = int(pi_value)
print(int_conversion)
print(type(int_conversion))

#str to int
str_num="123" 
print(type(str_num))
num = int(str_num)
print(num)
print(type(num))

#Task7-using input functions

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello,", name + "!")  
print("You are", age, "years old.")