from teacher.interfaces import ITeacher


class Teacher(ITeacher):
    def __init__(self, name: str, courses: list[str]):
        self.name = name
        self.courses = courses

    def __str__(self) -> str:
        return f'''
        Name: {self.name}
        Courses: {self.courses}
        '''

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses
