student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88,
}
student_name = input("Enter a student's name to see their marks: ")
marks = student_marks.get(student_name)

if marks is not None:
    print(f"The marks for {student_name} are: {marks}")
else:
    print(f"Error: Student '{student_name}' not found.")
