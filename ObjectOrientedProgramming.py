# Unit-IV Object Oriented Programming: Use of classes, inheritance, and operator overloading in problem solving.

# --- Unit IV: Object-Oriented Programming ---

# Base Class: Shape
class Shape:
    def __init__(self, color):
        self.color = color

    def display(self):
        print(f"Shape with color: {self.color}")

# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def display(self):
        print(f"Rectangle with color {self.color}, width {self.width}, and height {self.height}")

# Derived Class: Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def display(self):
        print(f"Circle with color {self.color} and radius {self.radius}")

# Operator Overloading: ComplexNumber Class
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Adding two complex numbers using the '+' operator
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    # String representation of the complex number
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# --- Main Program ---
def main():
    # Shape and its derived classes
    print("Object-Oriented Programming: Use of Classes, Inheritance, and Operator Overloading")
    
    # Rectangle Object
    rectangle = Rectangle("Red", 5, 8)
    rectangle.display()
    print(f"Area of Rectangle: {rectangle.area()}")

    # Circle Object
    circle = Circle("Blue", 3)
    circle.display()
    print(f"Area of Circle: {circle.area()}")
    
    # Operator Overloading
    num1 = ComplexNumber(3, 4)
    num2 = ComplexNumber(1, 2)
    
    # Adding complex numbers
    num3 = num1 + num2
    print(f"Sum of complex numbers: {num3}")

if __name__ == "__main__":
    main()
