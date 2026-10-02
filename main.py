students = []
attendance = {}


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students registered.")
        return

    print("\n--- Student List ---")

    for student in students:
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("-------------------")


def mark_attendance():
    if not students:
        print("No students registered.")
        return

    print("\n--- Mark Attendance ---")

    for student in students:
        choice = input(
            f"Is {student['name']} (Roll No: {student['roll_no']}) present? (y/n): "
        )

        if choice.lower() == "y":
            attendance[student["roll_no"]] = "Present"
        else:
            attendance[student["roll_no"]] = "Absent"

    print("Attendance marked successfully!")


while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")