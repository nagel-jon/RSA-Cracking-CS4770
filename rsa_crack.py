import sys

def read_input():
    lines = sys.stdin.buffer.readlines()  # Read all lines from stdin
    ascii_values = []  # Initialize an empty list to store ASCII values

    # Iterate through all but the last line to print and store ASCII values
    for line in lines[:-1]:
        for byte in line:
            ascii_values.append(byte)

    # Process the last line to extract two integers
    last_line = lines[-1].strip()  # Get the last line and strip whitespace
    integers = list(map(int, last_line.split()))  # Split and convert to integers

    if len(integers) == 2:
        print(f"Stored integers: {integers[0]}, {integers[1]}")
    else:
        print("Last line must contain exactly two integers.")

    # Print the stored ASCII values
    print(f"Stored ASCII values: {ascii_values}")

    # Convert the integers from string to int
    e = integers[0]  # First integer
    n = integers[1]  # Second integer

    return ascii_values, e, n

def rsa_decrypt(ciphertext, e, n):
    # Factor n to get p and q
    p = 0
    q = 0

    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break
    
    print(f"p: {p}")
    print(f"q: {q}")

    # Compute Euler's totient function
    phi = (p - 1) * (q - 1)
    print(f"phi: {phi}")

    # Compute private key
    d = 0
    for i in range(2, phi):
        if (i * e) % phi == 1:
            d = i
            break
    
    print(f"Private key: {d}")

    # Decrypt the ciphertext
    decrypted_message = []
    for c in ciphertext:
        m = modular_exponentiation(c, d, n)
        decrypted_message.append(m)
    
    # Convert decrypted ASCII values back to characters and print the message
    decrypted_chars = ''.join(chr(m) for m in decrypted_message)
    print("Decrypted message:", decrypted_chars)

def modular_exponentiation(base, exp, mod):
    # Perform modular exponentiation: base^exp % mod using the "square and multiply" method
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with the result
            result = (result * base) % mod
        exp = exp >> 1    # Right shift the exponent by 1
        base = (base * base) % mod  # Square the base
    return result

if __name__ == "__main__":
    encrypted_string, e, n = read_input()
    print(f"Integer 1: {e}")
    print(f"Integer 2: {n}")

    print("Cracking the RSA encryption...")

    rsa_decrypt(encrypted_string, e, n)
