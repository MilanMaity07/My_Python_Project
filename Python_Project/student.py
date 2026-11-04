class Student:

    def __init__(self, roll_no, name, marks, total_classes, attended_classes):

        self.roll_no = roll_no
        self.name = name
        self.marks = marks

        self.total = sum(marks)

        self.average = self.total / len(marks)

        self.percentage = self.average

        # Grade calculation
        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

        # Attendance calculation
        if total_classes > 0:
            self.attendance = (
                attended_classes / total_classes
            ) * 100
        else:
            self.attendance = 0


    def display(self):

        print("\n----------------------------")

        print("Roll No     :", self.roll_no)
        print("Name        :", self.name)

        print("Python      :", self.marks[0])
        print("DBMS        :", self.marks[1])
        print("Math        :", self.marks[2])
        print("AI          :", self.marks[3])

        print("Total       :", self.total)

        print(
            "Average     :",
            round(self.average, 2)
        )

        print(
            "Percentage  :",
            round(self.percentage, 2),
            "%"
        )

        print("Grade       :", self.grade)

        print(
            "Attendance  :",
            round(self.attendance, 2),
            "%"
        )

        print("----------------------------")