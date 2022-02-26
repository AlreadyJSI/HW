class Fraction:
    def __init__(self, up=0, down=0):
        self.numerator = up
        self.denumerator = down

    def input(self):
        self.numerator = int(input("Введите числитель:"))
        self.denumerator = int(input("Введите знаменатель:"))
        if self.denumerator == 0:
            raise ValueError('Знаменатель равен нулю')

    def __str__(self):
        return f"{self.numerator}/{self.denumerator}"


d1 = Fraction()
print(d1)

d2 = Fraction(11, 15)
print(d2)

d3 = Fraction()
d3.input()
print(d3)
