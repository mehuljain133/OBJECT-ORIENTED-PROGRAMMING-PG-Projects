# Unit-VI Exception Handling and File Handling: Reading and writing text and structured files, errors and exceptions.

import csv

# --- Exception Handling ---
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

# --- File Handling: Reading and Writing Text Files ---
def write_text_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Text successfully written to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File Content:\n{content}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# --- File Handling: Reading and Writing Structured Files (CSV) ---
def write_csv_file(filename, data):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'City'])  # Writing headers
            writer.writerows(data)
        print(f"CSV file {filename} written successfully.")
    except Exception as e:
        print(f"Error writing CSV file: {e}")

def read_csv_file(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header
            print(f"CSV File Content:")
            for row in reader:
                print(row)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# --- Main Program ---
def main():
    # Exception Handling Example
    print("\nException Handling Example:")
    result = divide_numbers(10, 2)
    if result is not None:
        print(f"10 / 2 = {result}")
    
    # Writing and Reading Text Files
    text_file = "sample_text.txt"
    content = "Hello, this is a sample text file.\nIt contains multiple lines of text."
    write_text_file(text_file, content)
    read_text_file(text_file)

    # Writing and Reading CSV Files
    csv_file = "sample_data.csv"
    data = [
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ]
    write_csv_file(csv_file, data)
    read_csv_file(csv_file)

if __name__ == "__main__":
    main()
