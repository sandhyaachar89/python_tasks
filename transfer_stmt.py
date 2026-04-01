#Q1-Write a Python program that takes a list of numbers as input numbers = [25, 30, 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100".

numbers = [25, 30, 20, 40, 15, 25]
total = 0

for num in numbers:
    total += num
    if total > 100:
        print("Sum exceeded 100")
        break
else:
    print("Total sum:", total)

#Q2-Write a Python script that uses a for loop to iterate through numbers from 1 to 600. Print only the odd numbers, skipping the even ones using the continue statement.

for i in range(1,600,2):
    print(i)

#Q3-Write a Python script that checks if a number is even or odd. If the number is even, print "Even"; if odd, do nothing (use the pass statement).

number=int(input("Enter the number:"))  
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")
    pass

#Q4-Write a Python script that iterates through a list of words. If the word is "break,"exit the loop using the break statement. If the word is "skip," skip the rest of the code for the current iteration using the continue statement. For any other word, print the word

words=["India", "Japan", "USA", "skip", "Russia", "break", "Germany", "Europe"]

for word in words:
    if word =="break":
        break
    elif word == "skip":
        continue
    else:
        print(word)
