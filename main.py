import sqlite3

# Connect to database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no TEXT PRIMARY KEY,
    name TEXT NOT NULL
)
""")

conn.commit()


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    try:
        cursor.execute(
            "INSERT INTO students (roll_no, name) VALUES (?, ?)",
            (roll_no, name)
        )

        conn.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Student with this roll number already exists.")


def view_students():
    cursor.execute("SELECT roll_no, name FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students registered.")
        return

    print("\n--- Student List ---")

    for student in students:
        print("Roll No:", student[0])
        print("Name:", student[1])
        print("-------------------")


def search_student():
    roll_no = input("Enter roll number to search: ")

    cursor.execute(
        "SELECT roll_no, name FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if student:
        print("\n--- Student Found ---")
        print("Roll No:", student[0])
        print("Name:", student[1])
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")

    cursor.execute(
        "SELECT roll_no FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    new_name = input("Enter new student name: ")

    cursor.execute(
        "UPDATE students SET name = ? WHERE roll_no = ?",
        (new_name, roll_no)
    )

    conn.commit()

    print("Student updated successfully!")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    cursor.execute(
        "SELECT roll_no FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    cursor.execute(
        "DELETE FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    conn.commit()

    print("Student deleted successfully!")


def mark_attendance():
    print("\nAttendance feature will be connected to database next.")


def view_attendance():
    print("\nAttendance report will be connected to database next.")


def attendance_percentage():
    print("\nAttendance percentage will be connected to database next.")


while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Update Student")
    print("8. Attendance Percentage")
    print("9. Exit")

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
        attendance_percentage()

    elif choice == "9":
        print("Thank you!")
        conn.close()
        break

    else:
        print("Invalid choice! Please try again.")