students = {}

# Add student
name = input("Enter student name: ")
grade = input("Enter grade: ")
students[name] = grade

# Update grade
update_name = input("Enter student name to update: ")

if update_name in students:
    new_grade = input("Enter new grade: ")
    students[update_name] = new_grade
else:
    print("Student not found.")

# Display all students
print("\nStudent Grades:")
for name, grade in students.items():
    print(name, ":", grade)