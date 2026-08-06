print("***** Student Management System *****")

students = {}

while True:
    name = input("\nEnter Student Name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    marks = []

    while True:
        mark = input("Enter Mark (or type 'done' to finish marks): ")

        if mark.lower() == "done":
            break

        marks.append(float(mark))

    students[name] = marks

print("\n========== STUDENT REPORT ==========")

for name, marks in students.items():
    print("\nStudent Name :", name)
    print("Marks :", marks)

    if len(marks) > 0:
        average = sum(marks) / len(marks)

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Average :", round(average, 2))
        print("Grade :", grade)
    else:
        print("No marks entered.")