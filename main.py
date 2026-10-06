import sqlite3
from datetime import date

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

# Create attendance table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no TEXT NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (roll_no) REFERENCES students(roll_no)
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
    today = str(date.today())

    cursor.execute("SELECT roll_no, name FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students registered.")
        return

    print("\n--- Mark Attendance ---")
    print("Date:", today)

    for student in students:
        roll_no = student[0]
        name = student[1]

        print("\nRoll No:", roll_no)
        print("Name:", name)

        status = input("Enter P for Present / A for Absent: ").upper()

        while status not in ["P", "A"]:
            print("Invalid choice!")
            status = input("Enter P for Present / A for Absent: ").upper()

        if status == "P":
            attendance_status = "Present"
        else:
            attendance_status = "Absent"

        # Check if attendance is already marked today
        cursor.execute(
            """
            SELECT id FROM attendance
            WHERE roll_no = ? AND date = ?
            """,
            (roll_no, today)
        )

        existing = cursor.fetchone()

        if existing:
            cursor.execute(
                """
                UPDATE attendance
                SET status = ?
                WHERE roll_no = ? AND date = ?
                """,
                (attendance_status, roll_no, today)
            )
        else:
            cursor.execute(
                """
                INSERT INTO attendance (roll_no, date, status)
                VALUES (?, ?, ?)
                """,
                (roll_no, today, attendance_status)
            )

    conn.commit()
    print("\nAttendance marked successfully!")


def view_attendance():
    cursor.execute("""
        SELECT attendance.roll_no,
               students.name,
               attendance.date,
               attendance.status
        FROM attendance
        JOIN students
        ON attendance.roll_no = students.roll_no
        ORDER BY attendance.date
    """)

    records = cursor.fetchall()

    if not records:
        print("\nNo attendance records found.")
        return

    print("\n--- Attendance Report ---")

    for record in records:
        print("Roll No:", record[0])
        print("Name:", record[1])
        print("Date:", record[2])
        print("Status:", record[3])
        print("------------------------")


def attendance_percentage():
    roll_no = input("Enter roll number: ")

    cursor.execute(
        "SELECT name FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    cursor.execute(
        """
        SELECT
            COUNT(*) AS total,
            SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END)
        FROM attendance
        WHERE roll_no = ?
        """,
        (roll_no,)
    )

    result = cursor.fetchone()

    total = result[0]
    present = result[1] or 0

    if total == 0:
        print("No attendance records found.")
        return

    percentage = (present / total) * 100

    print("\n--- Attendance Percentage ---")
    print("Roll No:", roll_no)
    print("Name:", student[0])
    print("Total Classes:", total)
    print("Present:", present)
    print("Absent:", total - present)
    print("Attendance Percentage:", round(percentage, 2), "%")


# Main menu
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