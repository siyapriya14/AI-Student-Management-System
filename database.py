import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER,
    attendance INTEGER
)
""")

conn.commit()


def add_student(name, age, course, marks, attendance):

    cursor.execute(
        """
        INSERT INTO students
        (name, age, course, marks, attendance)
        VALUES (?, ?, ?, ?, ?)
        """,
        (name, age, course, marks, attendance)
    )

    conn.commit()


def get_students():

    cursor.execute("SELECT * FROM students")

    return cursor.fetchall()


def delete_student(student_id):

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()


def update_student(student_id, name, age, course, marks, attendance):

    cursor.execute("""
    UPDATE students
    SET name=?,
        age=?,
        course=?,
        marks=?,
        attendance=?
    WHERE id=?
    """,
    (name, age, course, marks, attendance, student_id))

    conn.commit()