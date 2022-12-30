from abc import ABC, abstractmethod


class ICourse(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_teacher(self):
        pass

    @abstractmethod
    def get_course_program(self):
        pass


class ILocalCourse(ICourse):
    @abstractmethod
    def get_lab(self):
        pass


class IOffsiteCourse(ICourse):
    @abstractmethod
    def get_town(self):
        pass


class ICourseFactory(ABC):
    @abstractmethod
    def create_local_course(self, name, teacher, course_program, lab):
        pass

    @abstractmethod
    def create_offsite_course(self, name, teacher, course_program, town):
        pass
