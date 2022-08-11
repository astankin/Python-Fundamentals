class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        c = Circle.__pi * self.diameter
        return c

    def calculate_area(self):
        area = Circle.__pi * pow(self.radius, 2)
        return area

    def calculate_area_of_sector(self, angle):
        sector_area = pow(self.radius, 2) * (angle / 360) * Circle.__pi
        return sector_area


diameter = float(input())

circle = Circle(diameter)
angle = int(input())

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
