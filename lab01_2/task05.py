class Student:
    def __init__(self, name: str, surname: str, rbnum: int, grades: list):
        self.name = name
        self.surname = surname
        self.rbnum = rbnum
        self.grades = grades
        self.rating = sum(grades) / len(grades)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, students: list, max_students=20):
        temp = {}
        self.name = name
        self.max_students = max_students
        self.students = []
        for student in students:
            key = str(student)
            if not temp.get(key) and len(self.students) <= max_students:
                self.students.append(student)
                temp[key] = 1
            elif len(self.students) > max_students:
                raise ValueError(
                    f"The number of students in group {self.name} is more than the max_students amount"
                )

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError("You can only add students")
        for pupil in self.students:
            if pupil.name == student.name and pupil.surname == student.surname:
                raise ValueError(f"Student {student} is already in {self.name} group")
        if len(self.students) <= self.max_students:
            self.students.append(student)
        else:
            raise ValueError(f"Can't add student ${student}, group if fulfilled")

    def top_students(self):
        self.students.sort(key=lambda student: -student.rating)
        return self.students[:5]
