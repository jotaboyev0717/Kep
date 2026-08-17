class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.age, self.name) == (other.age, other.name)

    def __ne__(self, other):
        return (self.age, self.name) != (other.age, other.name)

    def __lt__(self, other):
        return (self.age, self.name) < (other.age, other.name)

    def __le__(self, other):
        return (self.age, self.name) <= (other.age, other.name)

    def __gt__(self, other):
        return (self.age, self.name) > (other.age, other.name)

    def __ge__(self, other):
        return (self.age, self.name) >= (other.age, other.name)