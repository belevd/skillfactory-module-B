class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age

h = Human()
h.set_age(15)
print(h.age)