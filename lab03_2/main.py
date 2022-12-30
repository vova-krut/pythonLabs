from course.classes import CourseFactory
from teacher.classes import Teacher

factory = CourseFactory()

teacher = Teacher(
    "John Smith", ["JavaScript Programming", "Python Programming"])

course = factory.create_local_course("JavaScript Programming", teacher, [
                                     "Introduction to JavaScript", "Event loop in Node.Js"], "Student lab 1")

print(course)
print(teacher)
