marks = int(input("Enter the marks: "))

if marks >=90:
    grade = 'A'
    print(grade)

elif marks >=80:
    grade = 'B'
    print(grade)
elif marks >=70:
    grade = 'C'
    print(grade)
elif marks >=60:
    grade = 'D'
    print(grade)
else:
    grade = 'F'
    print(grade)

# 2 Question
student = {"Rohit": 90, "Priya": 85, "Amit": 78, "Neha": 88}

# get input from user to add a new student and their marks to student dictionary
new_student = input("Enter the name of the new student: ")
new_marks = int(input("Enter the marks of the new student: "))
student[new_student] = new_marks

print(student)

# update any existing student's marks
update_student = input("Enter the name of the student to update marks: ")
if update_student in student:
    new_marks = int(input(f"Enter the new marks for {update_student}: "))
    student[update_student] = new_marks
    print(student)

# Print all student grades
for name, marks in student.items():
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"{name}: {grade}")


