from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return 4 * self.__side_length

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

shapes_list = [
    Square(4),
    Circle(3),
    Rectangle(5, 2)
]

for shape in shapes_list:
    print(f"Фігура: {shape.__class__.__name__}")
    print(f"- Площа: {shape.area():.2f}")
    print(f"- Периметр: {shape.perimeter():.2f}")
    print("_" * 30)