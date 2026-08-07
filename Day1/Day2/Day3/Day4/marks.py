def markscard():
    student_name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    english = int(input("Enter English Marks: "))
    kannada = int(input("Enter Kannada Marks: "))
    maths = int(input("Enter Mathematics Marks: "))
    science = int(input("Enter Science Marks: "))
    social = int(input("Enter Social Science Marks: "))

    total = english + kannada + maths + science + social
    max_marks = 500
    percentage = (total / max_marks) * 100

    print("\n========== MARKS CARD ==========")
    print("Student Name :", student_name)
    print("Roll Number  :", roll_no)
    print("--------------------------------------")
    print("Subject\t\t\tMarks")
    print("--------------------------------------")
    print("English\t\t\t", english)
    print("Kannada\t\t\t", kannada)
    print("Mathematics\t\t", maths)
    print("Science\t\t\t", science)
    print("Social Science\t\t", social)
    print("--------------------------------------")
    print("Total Marks\t\t", total, "/", max_marks)
    print("Percentage\t\t", round(percentage, 2), "%")
    print("======================================")

# Function call
markscard()