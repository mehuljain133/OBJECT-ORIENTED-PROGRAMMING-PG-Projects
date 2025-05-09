# Unit-I Introduction: Notion of class, object, identifier, keyword, and literal; basic data types: int, float, string, Boolean; basic operators (arithmetic, relational, logical, assignment), standard libraries.

# --- Introduction to Object Oriented Programming in Python ---

# Keywords, Identifiers, and Literals
# Example of identifiers (variable names) and literals (fixed values)
name = "Alice"        # string literal
age = 25              # int literal
height = 5.6          # float literal
is_student = True     # Boolean literal

# --- Basic Data Types ---
print("Data Types Example:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# --- Basic Operators ---
print("\nOperators Example:")
# Arithmetic
print("Sum:", age + 5)
print("Product:", age * 2)
# Relational
print("Is age greater than 20?", age > 20)
# Logical
print("Is student and age > 20?", is_student and age > 20)
# Assignment
x = 10
x += 5
print("x after += 5:", x)

# --- Standard Libraries ---
import math
import random

print("\nStandard Library Example:")
print("Square root of 16:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))

# --- Notion of Class and Object ---
class Person:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def check_student_status(self):
        return "I am a student." if self.is_student else "I am not a student."

# Creating an object of the class
person1 = Person("Alice", 25, True)

print("\nClass and Object Example:")
print(person1.greet())
print(person1.check_student_status())
