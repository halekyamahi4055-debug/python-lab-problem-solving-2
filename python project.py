# STUDENT REGISTRY (DICTIONARY+TUPLE)

student_registry={
    1003: ("keerthanaa","CSE",2029),
    1015: ("Halekya","ECE",2029)
}
print("student registry")
print(student_registry)

# COURSE ENROLLMENT (DICTIONARY+SET)

course_enrollments={
    1003:{"PHYSICS","CHEMISTRY"},
    1015:{"PHYSICS","MATHS"}
}
print()
print("course_enrollments")
print(course_enrollments)

# ADDING COURSE USING SET

course_enrollments[1003].add("BIOLOGY")

print()
print("updated courses")
print(course_enrollments[1003])

# COMMON COURSE USING INTERSECTION

common=course_enrollments[1003].intersection(course_enrollments[1015])

print()
print("common courses")
print(common)

# GRADE BOOKS (DICTIONARY+LIST OF TUPLES)

grade_books={
    1003:[("PHYSICS",90),("CHEMISTRY",84)],
    1015:[("PHYSICS",85),("MATHS",95)]
}
print()
print("grade books")
print(grade_books)

# GPA CALCULATION
grades=grade_books[1003]
total=0
for course,mark in grades:
    total=total+mark
average=total/len(grades)
print()
print("average marks of student 1003")
print(average)

# REGISTRY AUDITOR

print()
print("student report")
for student_id,details in student_registry.items():
    name=details[0]
    courses=course_enrollments[student_id]
    print(name,":",courses)





    
