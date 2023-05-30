# a) Create an empty list called "shopping_list."
shopping_list = []

while True:
    # b) Prompt the user to enter the items they want to buy and add each item to the shopping_list.
    item = input("Enter an item you want to buy (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)

# c) After the user finishes adding items, print the complete shopping_list.
print("\nYour Shopping List:")
for i in shopping_list:
    print(i)

# d) Using a loop, iterate over the shopping_list and display each item on a new line.
print("\nItems in the Shopping List:")
for item in shopping_list:
    print(item)

# e) Calculate and print the total number of items in the shopping_list.
print(f"\nTotal number of items in the shopping list: {len(shopping_list)}")

# f) Remove any item from the shopping_list that the user doesn't want to buy anymore and print the updated list.
while True:
    remove_item = input("\nEnter any item you don't want to buy anymore (or 'done' to finish): ")
    if remove_item.lower() == 'done':
        break
    if remove_item in shopping_list:
        shopping_list.remove(remove_item)
        print(f"Removed {remove_item} from the list.")
    else:
        print(f"{remove_item} is not in the list.")

print("\nUpdated Shopping List:")
for item in shopping_list:
    print(item)

# g) Finally, sort the shopping_list in alphabetical order and print it.
shopping_list.sort()
print("\nSorted Shopping List:")
for item in shopping_list:
    print(item)
