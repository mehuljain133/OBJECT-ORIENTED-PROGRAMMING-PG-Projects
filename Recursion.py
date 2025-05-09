# Unit-III Recursion: Use of recursion as a programming paradigm for problem solving

# --- Unit III: Recursion ---

# 1. Factorial (Basic Recursion)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 2. Fibonacci Sequence (Recursive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3. Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# 4. Reverse a String
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

# 5. Power of a Number (a^b)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

# 6. GCD (Greatest Common Divisor)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 7. Tower of Hanoi
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination)

# --- Main Program ---
def main():
    print("Recursion Examples:")

    print("\n1. Factorial of 5:", factorial(5))
    print("2. 7th Fibonacci number:", fibonacci(7))
    print("3. Sum of digits of 1234:", sum_of_digits(1234))
    print("4. Reverse of 'hello':", reverse_string("hello"))
    print("5. 2 raised to power 5:", power(2, 5))
    print("6. GCD of 48 and 18:", gcd(48, 18))

    print("\n7. Tower of Hanoi for 3 disks:")
    tower_of_hanoi(3, "A", "B", "C")

if __name__ == "__main__":
    main()
