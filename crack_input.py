import sys

def read_input():
    input_data = sys.stdin.read()  # Read all input from stdin
    lines = input_data.splitlines()  # Split the input into lines

    if len(lines) < 2:
        raise ValueError("Expected at least two lines of input.")

    encrypted_string = lines[0].strip()  # First line is the encrypted string

    # Split the last line into integers
    last_line = lines[-1].strip().split()  # Get the last line and split it into components
    if len(last_line) < 2:
        raise ValueError("Expected two integers in the last line.")

    # Convert the integers from string to int
    int1 = int(last_line[0])  # First integer
    int2 = int(last_line[1])  # Second integer

    return encrypted_string, int1, int2

if __name__ == "__main__":
    encrypted_string, int1, int2 = read_input()
    print(f"Encrypted String: {encrypted_string}")
    print(f"Integer 1: {int1}")
    print(f"Integer 2: {int2}")
