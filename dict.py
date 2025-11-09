#Q1-Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
my_dict["city"]="Banglore" 
print(my_dict)

#Q2Write Python code to access and print the value associated with the key 'price' in the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info["price"])

#Q3-Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop("city")
print(my_dict)

#Q4-Write Python code to print all the keys present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(list(my_dict.keys()))

#Q5-Write Python code to print all the values present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(list(my_dict.values()))

#----------------------------------------------------------------------------------

# Exercise 1:Write a Python script that updates a dictionary with a new key-value pair.
my_dict = {'name': 'sandhya', 'age': 25}
my_dict['city'] = 'Banglore'
print("After adding new key-value pair:", my_dict)

# Exercise 2: Access and print value associated with a specific key
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 120000}
print("Value of 'price':", product_info['price'])

# Exercise 3: Remove a key-value pair from a dictionary
my_dict2 = {'name': 'John', 'age': 30, 'city': 'Bhimavaram'}
my_dict2.pop('city')
print("After removing 'city':", my_dict2)

# Exercise 4: Print all keys present in a dictionary
my_dict3 = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print("Keys in dictionary:", list(my_dict3.keys()))

# Exercise 5: Print all values present in a dictionary
my_dict4 = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print("Values in dictionary:", list(my_dict4.values()))
