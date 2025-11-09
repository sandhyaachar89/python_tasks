dictionary = {}

while True:
    print("\nDictionary Management System")
    print("1. Add a word")
    print("2. Serach for Meaning")
    print("3. Display all words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter the word: ").lower()
        meaning = input("Enter the meaning: ")
        dictionary[word] = meaning
        print("Word added successfully!")

    elif choice == "2":
        word = input("Enter the word to search: ").lower()
        if word in dictionary:
            print("Meaning:",dictionary[word])
        else:
            print("word not found in dictionary.")
    
    elif choice == "3":
        if dictionary:
            print("all words in dictionary")
            for word, meaning in dictionary.items():
             print(f"{word} : {meaning}")
        else:
           print("Dictionary is empty.")

    elif choice == "4":
        word = input("Enter the word to update: ").lower()
        if word in dictionary:
            new_meaning = input("Enter new meaning:")
            dictionary[word] = new_meaning
            print("new meaning updated!")
        else:
            print("word not found in dictionary.")
    
    elif choice == "5":
        word = input("Enter the word to be delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print(f"The word {word} has been deleted!")
        else:
            print("word not found in dictionary.")    
    
    elif choice == "6":
        print("exiting the program...")
        break
    else:
        print("Invalid option, please select the option between 1-6")

    
    

   
          
                
            
             

        

