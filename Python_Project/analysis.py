import pandas as pd
import numpy as np


# ==============================
# SAVE DATA
# ==============================

def save_data(students):

    if len(students) == 0:

        print("\nNo student data to save.")

        return

    data = []

    for s in students:

        data.append({

            "Roll No": s.roll_no,

            "Name": s.name,

            "Python": s.marks[0],

            "DBMS": s.marks[1],

            "Math": s.marks[2],

            "AI": s.marks[3],

            "Total": s.total,

            "Average": round(s.average, 2),

            "Percentage": round(s.percentage, 2),

            "Grade": s.grade,

            "Attendance": round(s.attendance, 2)

        })

    df = pd.DataFrame(data)

    df.to_csv(
        "students.csv",
        index=False
    )

    print("\nData saved successfully!")


# ==============================
# READ CSV DATA
# ==============================

def read_data():

    try:

        df = pd.read_csv("students.csv")

        if df.empty:

            print("\nCSV file is empty.")

            print(
                "Please add students and "
                "save the data first."
            )

            return None

        print("\n====================================")
        print("        STUDENT CSV RECORDS")
        print("====================================")

        print(df.to_string(index=False))

        return df

    except FileNotFoundError:

        print("\nstudents.csv file not found.")

        return None

    except pd.errors.EmptyDataError:

        print("\nstudents.csv is empty.")

        return None


# ==============================
# LOW ATTENDANCE
# ==============================

def low_attendance(students, threshold):

    if len(students) == 0:

        print("\nNo student data available.")

        return

    print(
        f"\n===== STUDENTS BELOW {threshold}% ATTENDANCE ====="
    )

    found = False

    for student in students:

        if student.attendance < threshold:

            print(
                student.roll_no,
                "-",
                student.name,
                "-",
                round(student.attendance, 2),
                "%"
            )

            found = True

    if not found:

        print(
            "No student found below the threshold."
        )


# ==============================
# SORT STUDENTS
# ==============================

def sort_students(students):

    if len(students) == 0:

        print("\nNo student data available.")

        return

    sorted_students = sorted(
        students,
        key=lambda x: x.total,
        reverse=True
    )

    print("\n====================================")
    print("       STUDENTS SORTED BY MARKS")
    print("====================================")

    for i, student in enumerate(
        sorted_students,
        start=1
    ):

        print(
            i,
            ".",
            student.name,
            "- Total:",
            student.total
        )


# ==============================
# STATISTICS
# ==============================

def calculate_statistics(students):

    if len(students) == 0:

        print("\nNo student data available.")

        return

    totals = []

    percentages = []

    attendance = []

    for student in students:

        totals.append(student.total)

        percentages.append(
            student.percentage
        )

        attendance.append(
            student.attendance
        )

    totals = np.array(totals)

    percentages = np.array(percentages)

    attendance = np.array(attendance)

    print("\n====================================")
    print("            STATISTICS")
    print("====================================")

    print(
        "Highest Total Marks :",
        np.max(totals)
    )

    print(
        "Lowest Total Marks  :",
        np.min(totals)
    )

    print(
        "Average Total Marks :",
        round(np.mean(totals), 2)
    )

    print(
        "Average Percentage  :",
        round(np.mean(percentages), 2),
        "%"
    )

    print(
        "Average Attendance  :",
        round(np.mean(attendance), 2),
        "%"
    )