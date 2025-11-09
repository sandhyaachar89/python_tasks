#Q1-Write Python code to reverse the order of elements in the given list my_list .Print the reversed list.
'''my_list = [10, 20, 30, 40, 50, 11]
print(my_list[::-1])

#2nd way
my_list.reverse()
print(my_list)

#Q2-Given two lists list1 and list2 , find and print the common elements between them.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_num=[list(set(list1) & set(list2))]
print(common_num)

#Q3-Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print("Unique list:", unique_list)

#Q4-Remove duplicate elements from the given list duplicated_list and print the list without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = []
for item in duplicated_list:
    if item not in no_duplicates:
        no_duplicates.append(item)
print("List without duplicates:", no_duplicates)

#Exercise 1: List Concatenation
#Write a Python script that concatenates two lists and prints the result.
#list_1=[10,20,30,40]
#list_2=[50,60,70,80]
#new_list=list_1 + list_2
#print(new_list)

#Exercise 2: List Repetition
#Write a Python script that repeats a list three times and prints the result.
#list_1=[1,2,3,4]
#new=list_1*3
#print(new)

#Exercise 3: List Removal
#Write a Python script that removes the elements at even indices from a list.
#numbers = [10, 20, 30, 40, 50, 60, 70]
#result = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]
#print("List after removing even indices:", result)

#Exercise 4: List Insertion
#Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list.
#my_list = [1, 2, 3, 4, 5]
#my_list = [10, 11, 12] + my_list
#print("Updated list:", my_list)

#List comprehensions
#1. Square Numbers: Create a list of squares of numbers from 1 to 10.
#squares=[x**2 for x in range(1,11)]
#print(squares)

#2. Even Numbers: Generate a list of even numbers from 1 to 20.
#for i in range(0,11,2):
 #  print(i)

#3. Words Lengths: Given a list of words, create a list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date"]
lengths = [len(word) for word in words]
print("Word lengths:", lengths)'''