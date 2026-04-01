#Q1-Create a Tuple: Write a program that creates a tuple containing three elements: your name, your age, and your favorite color. Then print the tuple
tuple1 = ("sandhya",20,"purple")
print(tuple1)
print(type(tuple1))

#Q2-Access Tuple Elements: Write a program that creates a tuple containing the days of the week. Then, print the third element of the tuple.
tuple2 = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
print(tuple2[2])

#Q3-Tuple Concatenation: Write a program that creates two tuples, one containing odd numbers from 1 to 5 and another containing even numbers from 2 to 6. Concatenate these two tuples and print the result.
tuple_1 = (1,3,5)
tuple_2 = (2,4,6)
concat = tuple_1+tuple_2
print(concat)

#Q4-Tuple Unpacking: Write a program that defines a tuple containing the dimensions of a rectangle (length and width). Then, unpack this tuple into two variables and calculate the area of the rectangle.
tuple_1 = (15,5)
length,width = tuple_1 
area = length * width
print(f"length:",length)
print(f"width:",width)
print(f"Area of rectangle is :",area)

#Q5-Check if an Element Exists: Write a program that checks if a given element exists in a tuple.
countries = ("India","Japan","Europe","Russia","USA")
is_present = 'Japan' in countries
print(is_present)

#Q6-Write a Python program to generate a bill for a supermarket purchase. The program should store the items and their prices in a list of tuples. It should then iterate over this list to print out each item along with its price. Finally, calculate and print the total cost of all the items

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print("item\tprice")
print("-"*15)
total = 0
for item,price in items:
    print(f"{item}\t{price:.2f}")
    total += price
print("-"*15)
print(f"total:\t{total:.2f}")


    
