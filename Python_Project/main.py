from student import Student

from analysis import (
    save_data,
    read_data,
    low_attendance,
    sort_students,
    calculate_statistics
)

from charts import (
    show_bar_chart,
    show_line_graph,
    show_histogram
)


students = []


# ==========================================
# ADD STUDENT
# ==========================================

def add_student():

    try:

        print("\n===== ADD STUDENT =====")

        roll_no = input(
            "Enter Roll No: "
        )

        name = input(
            "Enter Student Name: "
        )

        print("\nEnter marks out of 100:")

        python = float(
            input("Python: ")
        )

        dbms = float(
            input("DBMS: ")
        )

        math = float(
            input("Math: ")
        )

        ai = float(
            input("AI: ")
        )

        # Check marks
        marks = [
            python,
            dbms,
            math,
            ai
        ]

        for mark in marks:

            if mark < 0 or mark > 100:

                print(
                    "Marks must be between 0 and 100."
                )

                return

        total_classes = int(
            input(
                "\nEnter Total Classes: "
            )
        )

        attended_classes = int(
            input(
                "Enter Attended Classes: "
            )
        )

        if attended_classes > total_classes:

            print(
                "Attended classes cannot be "
                "greater than total classes."
            )

            return

        student = Student(
            roll_no,
            name,
            marks,
            total_classes,
            attended_classes
        )

        students.append(student)

        print(
            "\nStudent added successfully!"
        )

        student.display()

    except ValueError:

        print(
            "\nInvalid input! "
            "Please enter numbers correctly."
        )


# ==========================================
# SHOW ALL STUDENTS
# ==========================================

def show_students():

    if len(students) == 0:

        print(
            "\nNo student records available."
        )

        return

    print(
        "\n===================================="
    )

    print(
        "          ALL STUDENTS"
    )

    print(
        "===================================="
    )

    for student in students:

        student.display()


# ==========================================
# GRAPH MENU
# ==========================================

def graph_menu():

    if len(students) == 0:

        print(
            "\nNo student data available."
        )

        print(
            "Please add and save students first."
        )

        return

    # Save latest data before graph
    save_data(students)

    while True:

        print("\n===== GRAPHICAL REPORTS =====")

        print("1. Bar Chart")
        print("2. Line Graph")
        print("3. Histogram")
        print("4. Back to Main Menu")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            show_bar_chart()

        elif choice == "2":

            show_line_graph()

        elif choice == "3":

            show_histogram()

        elif choice == "4":

            break

        else:

            print(
                "Invalid choice!"
            )


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("==========================================")
    print("   STUDENT PERFORMANCE & ATTENDANCE")
    print("              ANALYZER")
    print("==========================================")

    print("1. Add Student")
    print("2. Show Students")
    print("3. Low Attendance Students")
    print("4. Sort Students by Marks")
    print("5. Save Data")
    print("6. Read CSV Data")
    print("7. Statistics")
    print("8. Graphical Reports")
    print("9. Exit")

    choice = input(
        "\nEnter your choice: "
    )


    # ======================================
    # CHOICE 1
    # ======================================

    if choice == "1":

        add_student()


    # ======================================
    # CHOICE 2
    # ======================================

    elif choice == "2":

        show_students()


    # ======================================
    # CHOICE 3
    # ======================================

    elif choice == "3":

        try:

            threshold = float(
                input(
                    "Enter attendance threshold (%): "
                )
            )

            low_attendance(
                students,
                threshold
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )


    # ======================================
    # CHOICE 4
    # ======================================

    elif choice == "4":

        sort_students(students)


    # ======================================
    # CHOICE 5
    # ======================================

    elif choice == "5":

        save_data(students)


    # ======================================
    # CHOICE 6
    # ======================================

    elif choice == "6":

        read_data()


    # ======================================
    # CHOICE 7
    # ======================================

    elif choice == "7":

        calculate_statistics(
            students
        )


    # ======================================
    # CHOICE 8
    # ======================================

    elif choice == "8":

        graph_menu()


    # ======================================
    # CHOICE 9
    # ======================================

    elif choice == "9":

        print(
            "\nThank you for using "
            "Student Performance Analyzer!"
        )

        break


    else:

        print(
            "\nInvalid choice! "
            "Please enter 1 to 9."
        )