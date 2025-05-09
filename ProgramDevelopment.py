# Unit-II Program Development: Modular program development, input and output statements, controlstatements: branching, looping, exit function, break, continue, and switch-break; use of mutable andimmutable structures. strings, lists, sets, tuples and dictionary, and associated operations testing, anddebugging a program.

# --- Modular Program Development using Functions ---

def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def display_user_info(name, age):
    print(f"\nHello {name}, you are {age} years old.")

# --- Control Statements: Branching ---
def age_category(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

# --- Control Statements: Looping, break, continue, exit ---
def loop_demo():
    print("\nLoop Demo (print odd numbers up to 10, skip 5, stop at 9):")
    for i in range(1, 11):
        if i == 5:
            continue  # skip 5
        if i == 9:
            break  # stop at 9
        if i % 2 != 0:
            print(i, end=' ')
    print()

# Exit function demo (commented to avoid stopping the script)
# import sys
# def exit_demo():
#     sys.exit("Exit called")

# --- Mutable and Immutable Structures ---
def mutable_immutable_demo():
    print("\nMutable and Immutable Structures:")
    
    # Immutable: string, tuple
    s = "hello"
    print("Original string:", s)
    s = s.upper()
    print("Uppercased string (new object):", s)

    t = (1, 2, 3)
    print("Tuple (immutable):", t)

    # Mutable: list, set, dict
    lst = [1, 2, 3]
    lst.append(4)
    print("List after append:", lst)

    st = {1, 2, 3}
    st.add(4)
    print("Set after add:", st)

    dct = {"a": 1, "b": 2}
    dct["c"] = 3
    print("Dict after adding item:", dct)

# --- Data Structures and Operations ---

def structure_operations():
    print("\nStructure Operations:")
    my_string = "Python"
    print("String reverse:", my_string[::-1])

    my_list = [10, 20, 30]
    my_list.append(40)
    print("List:", my_list)

    my_set = set([1, 2, 3, 2])
    my_set.add(5)
    print("Set (no duplicates):", my_set)

    my_tuple = (5, 10, 15)
    print("Tuple sum:", sum(my_tuple))

    my_dict = {"apple": 10, "banana": 5}
    print("Dict keys:", list(my_dict.keys()))

# --- Program Testing and Debugging ---
def buggy_function(x):
    try:
        result = 10 / x
        return f"Result is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except Exception as e:
        return f"Unexpected error: {e}"

# --- Simulating Switch (using dictionary mapping) ---
def switch_demo(option):
    switch = {
        1: "Option 1 Selected",
        2: "Option 2 Selected",
        3: "Option 3 Selected"
    }
    return switch.get(option, "Invalid Option")

# --- Main Program ---

def main():
    name, age = get_user_info()
    display_user_info(name, age)
    
    category = age_category(age)
    print("You are classified as:", category)

    loop_demo()
    mutable_immutable_demo()
    structure_operations()

    print("\nTesting buggy_function with 0:", buggy_function(0))
    print("Testing buggy_function with 5:", buggy_function(5))

    print("\nSimulating switch-case:")
    print(switch_demo(2))

if __name__ == "__main__":
    main()

