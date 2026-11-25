class comp:
    brand = 'Acer'
    def __init__(self, model):
        self.model = model


    @classmethod
    def info(self):
        print(f"Brand: {self.brand}")
        print(f"Class: {self.__class__.__name__}")


c1 = comp("Aspire")
c1.info()
print(c1.brand)


c2 = comp("Predator")
c2.info()
print(c2.brand)