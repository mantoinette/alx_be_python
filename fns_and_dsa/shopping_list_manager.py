def display_menu():
  print(f"Shopping List Manager")  # Use f-string for title
  print(f"1. Add Item")  # Use f-string for menu option 1
  print(f"2. Remove Item")  # Use f-string for menu option 2
  print(f"3. View List")  # Use f-string for menu option 3
  print(f"4. Exit")  # Use f-string for menu option 4


def main():
  shopping_list = []
  while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

   if choice == '1':
  item_name = input(f"Enter the item to add: ")  # Use f-string for prompt
  shopping_list.append(item_name)
  print(f"{item_name} added to the list!")


    elif choice == '2':
      item = input("Enter the item name to remove: ").strip()
      if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
      else:
        print(f"'{item}' not found in the list.")

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
