class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
        self.__marks = marks or {}

    
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def calculate_result(self, subject=None, mark=None):
        if subject is not None and mark is not None:
            self.__marks[subject] = mark
            return f"{subject}: {mark}"

        if not self.__marks:
            return "No marks available."

        total = sum(self.__marks.values())
        average = total / len(self.__marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return f"Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "Student"

    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Student ID: {self.student_id}\n"
            f"Email: {self.get_email()}\n"
            f"Age: {self.age}\n"
            f"Department: {self.department}\n"
            f"Student Type: {self.get_student_type()}\n"
            f"Result: {self.calculate_result()}"
        )


class UndergraduateStudent(Student):
    def __init__(
        self, name, student_id, email, age, department,
        semester, marks=None
    ):
        super().__init__(
            name, student_id, email, age, department, marks
        )
        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        return (
            super().display_info()
            + f"\nSemester: {self.semester}"
        )


class GraduateStudent(Student):
    def __init__(
        self, name, student_id, email, age, department,
        research_topic, marks=None
    ):
        super().__init__(
            name, student_id, email, age, department, marks
        )
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        return (
            super().display_info()
            + f"\nResearch Topic: {self.research_topic}"
        )


def main():

    undergraduate = UndergraduateStudent(
        name="Ishtiaq Ahmed",
        student_id="ST001",
        email="ahmed@gmail.com",
        age=21,
        department="Computer Science",
        semester=6,
        marks={
            "Python": 85,
            "Database": 78,
            "Web Development": 88
        }
    )

    graduate = GraduateStudent(
        name="Ishtiaq Hossain",
        student_id="ST002",
        email="ishtiaq@gmail.com",
        age=26,
        department="Computer Science",
        research_topic="Artificial Intelligence",
        marks={
            "Machine Learning": 91,
            "Deep Learning": 87,
            "Research Methodology": 82
        }
    )

    print("Adding another undergraduate mark:")
    print(undergraduate.calculate_result("OOP", 90))
    print()

    students = [undergraduate, graduate]

    print("=" * 50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    for student in students:
        print(student.display_info())
        print("-" * 50)


if __name__ == "__main__":
    main()
