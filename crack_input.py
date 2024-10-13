def read_input_file(file_path):
    with open(file_path, 'rb') as file:  # Open the file in binary mode
        encrypted_bytes = file.readline().strip()  # Read the encrypted string
        encrypted_string = encrypted_bytes.decode('latin-1')  # Decode the encrypted string
        
        # Read the rest of the file to get the integers
        remaining_data = file.read().strip()  # Read the remaining bytes
        remaining_string = remaining_data.decode('latin-1')  # Decode the remaining bytes
        
        # Split the remaining string into lines and get the last line for integers
        lines = remaining_string.splitlines()
        if len(lines) < 1:
            raise ValueError("No lines found for integers.")

        # Split the last line into integers
        last_line = lines[-1].strip().split()  # Get the last line and split it into components
        if len(last_line) < 2:
            raise ValueError("Expected two integers in the last line.")

        # Convert the integers from string to int
        int1 = int(last_line[0])  # First integer
        int2 = int(last_line[1])  # Second integer

    return encrypted_string, int1, int2

if __name__ == "__main__":
    file_path = 'tests/easy/test_cracking_easy.input'
    encrypted_string, int1, int2 = read_input_file(file_path)
    print(f"Encrypted String: {encrypted_string}")
    print(f"Integer 1: {int1}")
    print(f"Integer 2: {int2}")
