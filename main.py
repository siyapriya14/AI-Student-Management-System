from tkinter import *
from tkinter import ttk

from database import *
from ai_helper import *

root = Tk()

root.title("AI Student Management Assistant")

root.geometry("900x600")

# =========================
# FUNCTIONS
# =========================

def add_data():

    name = name_entry.get()

    age = age_entry.get()

    course = course_entry.get()

    marks = marks_entry.get()

    attendance = attendance_entry.get()

    add_student(
        name,
        int(age),
        course,
        int(marks),
        int(attendance)
    )

    show_students()


def show_students():

    records = tree.get_children()

    for item in records:
        tree.delete(item)

    students = get_students()

    for student in students:

        remark = generate_remark(
            student[4],
            student[5]
        )

        tree.insert(
            "",
            END,
            values=(
                student[0],
                student[1],
                student[2],
                student[3],
                student[4],
                student[5],
                remark
            )
        )


def delete_data():

    selected = tree.focus()

    data = tree.item(selected)

    student_id = data['values'][0]

    delete_student(student_id)

    show_students()

# =========================
# LABELS
# =========================

Label(root, text="Name").place(x=20, y=20)

Label(root, text="Age").place(x=20, y=60)

Label(root, text="Course").place(x=20, y=100)

Label(root, text="Marks").place(x=20, y=140)

Label(root, text="Attendance").place(x=20, y=180)

# =========================
# ENTRY BOXES
# =========================

name_entry = Entry(root)

name_entry.place(x=120, y=20)

age_entry = Entry(root)

age_entry.place(x=120, y=60)

course_entry = Entry(root)

course_entry.place(x=120, y=100)

marks_entry = Entry(root)

marks_entry.place(x=120, y=140)

attendance_entry = Entry(root)

attendance_entry.place(x=120, y=180)

# =========================
# BUTTONS
# =========================

Button(
    root,
    text="Add Student",
    command=add_data
).place(x=40, y=240)

Button(
    root,
    text="Delete Student",
    command=delete_data
).place(x=150, y=240)

# =========================
# TABLE
# =========================

columns = (
    "ID",
    "Name",
    "Age",
    "Course",
    "Marks",
    "Attendance",
    "Remark"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for col in columns:
    tree.heading(col, text=col)

tree.place(x=320, y=20, width=550, height=500)

show_students()

root.mainloop()