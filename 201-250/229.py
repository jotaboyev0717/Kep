class Number(int):
    def digits_sum(self):
        return sum(int(d) for d in str(self))

number = Number(123)
print(number.real)
print(number.digits_sum())