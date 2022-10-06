import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator have to be int")
        if denominator == 0:
            raise ZeroDivisionError("Denominator can not be zero")
        self._numerator = numerator
        self._denominator = denominator

    def __str__(self):
        gcd = math.gcd(self._numerator, self._denominator)
        return f"{self._numerator // gcd}/{self._denominator // gcd}"

    def get_fraction(self):
        return self.__str__()

    def get_float(self):
        return self._numerator / self._denominator
