students = []
attendance = {}


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    # Check if roll number already exists
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this roll number already exists.")
            return

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
        roll_no = student["roll_no"]

        if roll_no not in attendance:
            attendance[roll_no] = {
                "total": 0,
                "present": 0,
                "absent": 0
            }

        choice = input(
            f"Is {student['name']} (Roll No: {roll_no}) present? (y/n): "
        )

        attendance[roll_no]["total"] += 1

        if choice.lower() == "y":
            attendance[roll_no]["present"] += 1
        elif choice.lower() == "n":
            attendance[roll_no]["absent"] += 1
        else:
            print("Invalid choice. Marked as Absent.")
            attendance[roll_no]["absent"] += 1

    print("Attendance marked successfully!")


def view_attendance():
    if not students:
        print("No students registered.")
        return

    print("\n--- Attendance Report ---")

    for student in students:
        roll_no = student["roll_no"]

        if roll_no not in attendance:
            print("Roll No:", roll_no)
            print("Name:", student["name"])
            print("Attendance: Not Marked")
            print("-------------------")
            continue

        total = attendance[roll_no]["total"]
        present = attendance[roll_no]["present"]
        absent = attendance[roll_no]["absent"]

        percentage = (present / total) * 100

        print("Roll No:", roll_no)
        print("Name:", student["name"])
        print("Total Classes:", total)
        print("Present:", present)
        print("Absent:", absent)
        print(f"Attendance: {percentage:.2f}%")
        print("-------------------")


def search_student():
    if not students:
        print("No students registered.")
        return

    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\n--- Student Found ---")
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])

            if roll_no in attendance:
                total = attendance[roll_no]["total"]
                present = attendance[roll_no]["present"]

                percentage = (present / total) * 100

                print(f"Attendance: {percentage:.2f}%")
            else:
                print("Attendance: Not Marked")

            return

    print("Student not found.")


def delete_student():
    if not students:
        print("No students registered.")
        return

    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)

            # Remove attendance record also
            if roll_no in attendance:
                del attendance[roll_no]

            print("Student deleted successfully!")
            return

    print("Student not found.")


def update_student():
    if not students:
        print("No students registered.")
        return

    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            new_name = input("Enter new student name: ")

            student["name"] = new_name

            print("Student updated successfully!")
            return

    print("Student not found.")


while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Update Student")
    print("8. Exit")

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
        search_student()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        update_student()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")