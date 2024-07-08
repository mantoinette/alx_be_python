# shopping_list_manager.py

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
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item_name = input("Enter the item to add: ").strip()
            shopping_list.append(item_name)
            print(f"'{item_name}' added to the list!")

        elif choice == '2':
            item_name = input("Enter the item name to remove: ").strip()
            if item_name in shopping_list:
                shopping_list.remove(item_name)
                print(f"'{item_name}' has been removed from the list.")
            else:
                print(f"'{item_name}' not found in the list.")

        elif choice == '3':
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
