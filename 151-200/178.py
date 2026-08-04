class Student():
    def __init__(self, name, age, balls):
        self.name = name
        self.age = age
        self.balls = balls

    def get_average_ball(self):
        if not self.balls:
            return 0
        return sum(self.balls) / len(self.balls)
