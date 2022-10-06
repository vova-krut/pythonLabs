import os


class TextStats:
    def __init__(self, filename: str):
        file_directory = os.getcwd() + os.sep + filename
        if not os.path.isfile(file_directory):
            raise ValueError(f"There is no such file {file_directory}")
        self._filename = filename

    def __str__(self):
        return f"""Chars: {self.count_chars()}, lines: {self.count_lines()}, 
        Sentences: {self.count_sentences()}, words: {self.count_words()}"""

    def count_chars(self):
        with open(self._filename) as file:
            line = file.readline()
            counter = 0
            while line:
                counter += len(line)
                line = file.readline()
            return counter

    def count_lines(self):
        with open(self._filename) as file:
            line = file.readline()
            counter = 0
            while line:
                counter += 1
                line = file.readline()
            return counter

    def count_sentences(self):
        with open(self._filename) as file:
            line = file.readline()
            counter = 0
            while line:
                for char in line:
                    if char == "." or char == "!" or char == "..." or char == "?":
                        counter += 1
                line = file.readline()
            return counter

    def count_words(self):
        with open(self._filename) as file:
            line = file.readline()
            counter = 0
            while line:
                counter += len(line.split(" "))
                line = file.readline()
            return counter
