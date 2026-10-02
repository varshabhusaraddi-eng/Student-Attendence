students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)

    print("Student added successfully!")


while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")