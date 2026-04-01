#Q1-Write Python code to find and print the intersection of the following two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)

#Q2-Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)

#Q3-Write Python code to find and print the elements present in set1 but not in set2.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.difference(set2)
print(set3)

#Q4-Write Python code to find and print the symmetric difference of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.symmetric_difference(set2)
print(set3)

#Q5-Write Python code to check if the element 3 is present in the set my_set :
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

Exercise 1: Set Intersection
Write a Python script that finds and prints the intersection of two sets.
Exercise 2: Set Union
Write a Python script that finds and prints the union of two sets.
Exercise 3: Set Difference
Write a Python script that finds and prints the difference between two sets.
Exercise 4: Set Symmetric Difference
Write a Python script that finds and prints the symmetric difference between
two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)
set3 = set1.intersection(set2)
print(set3)
set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1.difference(set2)
print(set3)


#SET OPERATIONS USING FROZEN SET
#UNION
set_1 = {25,5.7,"pythonlife",67,}
set_2 = frozenset(set_1)
print(set_2)
set_3 = {"tarun"}
res = set_1.union(set_3)
print(res)

#INTERSECTION
set_1 = {25,5.7,"pythonlife",67,99.00}
set_2 = frozenset(set_1)
print(set_2)
set_3 = {"tarun",25,"python",67}
res = set_1.intersection(set_3)
print(res)

#SYMMETRIC_DIFFERANCE
set_1 = {25,5.7,"pythonlife",67,99.00}
set_2 = frozenset(set_1)
print(set_2)
set_3 = {"tarun",25,"python",67}
res = set_1.symmetric_difference(set_3)
print(res)

#DIFFERANCE
set_1 = {25,5.7,"pythonlife",67,99.00}
set_2 = frozenset(set_1)
print(set_2)
set_3 = {"tarun",25,"python",67}
res = set_1.difference(set_3)
print(res)

