
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
        elif choice.lower() == "n":
            attendance[student["roll_no"]] = "Absent"
        else:
            print("Invalid choice. Marked as Absent.")
            attendance[student["roll_no"]] = "Absent"

    print("Attendance marked successfully!")


def view_attendance():
    if not students:
        print("No students registered.")
        return

    if not attendance:
        print("Attendance has not been marked yet.")
        return

    print("\n--- Attendance Report ---")

    for student in students:
        roll_no = student["roll_no"]
        status = attendance.get(roll_no, "Not Marked")

        print("Roll No:", roll_no)
        print("Name:", student["name"])
        print("Attendance:", status)
        print("-------------------")


while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        view_attendance()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
