# Creating a set
unique_numbers = {1, 2, 3, 4, 4, 4}
print(unique_numbers) # Output: {1, 2, 3, 4} (Duplicates removed!)
# Adding an item
unique_numbers.add(5)
# Removing an item
unique_numbers.discard(2)
# Checking if item exists
print(3 in unique_numbers) # Output: True
