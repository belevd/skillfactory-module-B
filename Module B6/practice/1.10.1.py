class Rectangle:

    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def as_str(self):
        return f'Rectangle ({self.x}, {self.y}, {self.width}, {self.height})'


rect_1 = Rectangle(5, 10, 50, 100)
print(rect_1.as_str())