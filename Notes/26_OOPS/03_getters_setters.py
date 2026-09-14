class student:
    def __init__(self, maths, english):
        self._maths = maths
        self.english = english


    @property
    def maths(self):
        return ((self._maths + self._english) / 200) * 100

    @maths.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._maths = value
        else:
            raise ValueError("Out of bounds marks")

s = student(101, 50)
