class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Number(self.number + other.number)

    def __str__(self):
        return str(self.number)