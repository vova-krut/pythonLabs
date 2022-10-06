class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("Length and width for rectangle have to be floats")
        self._length = length
        self._width = width

    def __str__(self):
        return f"""Length: {self._length}, width: {self._width}, 
        Periemeter: {self.calculate_perimeter()}, area: {self.calculate_area()}"""

    def get_length(self):
        return self._length

    def set_length(self, length: float):
        if not isinstance(length, float):
            raise TypeError("Length has to be float")
        if 0 < length < 20:
            self._length = length
        else:
            raise Exception("Length has to be between 0 and 20")

    def get_width(self):
        return self._width

    def set_width(self, width: float):
        if not isinstance(width, float):
            raise TypeError("Width has to be float")
        if 0 < width < 20:
            self._width = width
        else:
            raise Exception("Width has to be between 0 and 20")

    def calculate_perimeter(self):
        return (self._width + self._length) * 2

    def calculate_area(self):
        return self._length * self._width
