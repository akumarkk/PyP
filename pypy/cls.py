class Chai:
    def __init__(self, sweetness, pow):
        self.sweetness = sweetness
        self.pow = pow

    def add_sweetness(self, amount):
        self.sweetness += amount

    def add_pow(self, amount):
        self.pow += amount

    def __str__(self):
        return f"Chai(sweetness={self.sweetness}, pow={self.pow})"

c =Chai(5, 3)
print(c)
c.add_sweetness(2)
c.add_pow(1)
print(c)    