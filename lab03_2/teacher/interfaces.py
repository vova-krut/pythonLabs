from abc import ABC, abstractmethod


class ITeacher(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_courses(self):
        pass
