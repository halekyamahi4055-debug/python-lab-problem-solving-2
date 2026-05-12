# List Operations

numbers = [10, 20, 30, 40]

print("Original List:", numbers)

numbers.append(50)
print("After Append:", numbers)

numbers.insert(2, 25)
print("After Insert:", numbers)

numbers.remove(30)
print("After Remove:", numbers)

print("Length of List:", len(numbers))

print("List Elements:")
for item in numbers:
    print(item)
