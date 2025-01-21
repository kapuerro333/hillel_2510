import math

class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони a має бути більшою за 0")
        if name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут має становити від 0 до 180 градусів")
            super().__setattr__('angle_b', 180 - value)
        super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб: сторона = {self.side_a}, кут_а = {self.angle_a}, кут_б = {self.angle_b}"

romb = Romb(13, 5)
print(romb)