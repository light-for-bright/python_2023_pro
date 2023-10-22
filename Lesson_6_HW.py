# 1
class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print(f"Площадь прямоугольника равна: {self.a * self.b}")

    def perimeter(self):
        print(f"Периметр прямоугольника равен: {(self.a + self.b) * 2}")

rect_1 = Rectangle(5, 10)
rect_1.area()
rect_1.perimeter()

# 2
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Площадь круга равна: {3.14 * self.radius ** 2}")

    def perimeter(self):
        print(f"Периметр круга равен: {2 * 3.14 * self.radius}")

circle_1 = Circle(5)
circle_1.area()
circle_1.perimeter()

# 3
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Площадь треугольника равна: {0.5 * self.base * self.height}")

triangle_1 = Triangle(3, 4)
triangle_1.area()

# D.1
import turtle

t = turtle.Turtle()

class Rectangle_t(Rectangle):
    def draw(self):
        for i in range(2):
            t.forward(self.a)
            t.right(90)
            t.forward(self.b)
            t.right(90)


rect_2 = Rectangle_t(10, 20)
rect_2.draw()

class Circle_t(Circle):
    def draw(self):
        t.circle(self.radius)

circle_2 = Circle_t(100)
circle_2.draw()

# D.2
def draw_all(fig1, fig2):
    t.reset()
    fig1.draw()
    fig2.draw()

draw_all(rect_2, circle_2)
