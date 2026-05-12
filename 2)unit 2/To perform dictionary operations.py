student = {
    "Name": "Priya",
    "Age": 20,
    "Department": "CSE"
}

print(student)

student["Marks"] = 85

for key, value in student.items():
    print(key, ":", value)
