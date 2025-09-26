def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            shopping_item = input("Which item would you like to add to the list? ")
            shopping_list.append(shopping_item)
            print(f"The updated shopping list is {shopping_list}\n")
            pass
        elif choice == '2':
            print(shopping_list)
            remove = input("Which item do you want to remove?: ")
            shopping_list.remove(remove)
            print(f"The updated shopping list is {shopping_list}\n")
        elif choice == '3':
            print(f"This is your shopping list\n {shopping_list}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            
    

        