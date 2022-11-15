class Dates:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise TypeError("Day has to be an int")
        if value <= 0 or value > 31:
            raise ValueError("Day has to be between 1 and 31")
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise TypeError("Month has to be an int")
        if value <= 0 or value > 12:
            raise ValueError("Month has to be between 1 and 12")
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("Year has to be an int")
        if value <= 0:
            raise ValueError("Year has to be a positive int")
        self._year = value

    def get_full_date(self):
        monthes = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        return f"{self.day} {monthes.get(self.month)} {self.year} year"

    def get_short_date(self):
        return f"{self.day}.{self.month}.{self.year}"
