from course.interfaces import ICourseFactory, ICourse, ILocalCourse, IOffsiteCourse
from teacher.classes import Teacher


class CourseFactory(ICourseFactory):
    def create_local_course(self, name: str, teacher: Teacher, course_program: list[str], lab: str):
        return LocalCourse(name, teacher, course_program, lab)

    def create_offsite_course(self, name: str, teacher: Teacher, course_program: list[str], town: str):
        return OffsiteCourse(name, teacher, course_program, town)


class Course(ICourse):
    def __init__(self, name: str, teacher: Teacher, course_program: list[str]):
        self.name = name
        self.teacher = teacher
        self.course_program = course_program

    def __str__(self) -> str:
        return f'''
        Course: {self.name}
        Teacher: {self.teacher.name}
        Course Program: {self.course_program}        
        '''

    def get_name(self):
        return self.name

    def get_teacher(self):
        return self.teacher

    def get_course_program(self):
        return self.course_program


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name: str, teacher: Teacher, course_program: list[str], lab: str):
        super().__init__(name, teacher, course_program)
        self.lab = lab

    def __str__(self) -> str:
        return f'''
        {super().__str__()}
        Lab: {self.lab}
        '''

    def get_lab(self):
        return self.lab


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name: str, teacher: Teacher, course_program: list[str], town: str):
        super().__init__(name, teacher, course_program)
        self.town = town

    def __str__(self) -> str:
        return f'''
        {super().__str__()}
        Town: {self.town}
        '''

    def get_town(self):
        return self.town
