import sys

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

def rsa_encrypt(plaintext, e, n):
    # Encrypt each byte of the plaintext using RSA
    ciphertext = []
    for char in plaintext:
        m = ord(char)  # Get the ASCII value of the character
        c = modular_exponentiation(m, e, n)  # Compute the ciphertext as m^e % n
        ciphertext.append(str(c))  # Store the encrypted value as a string
    return ' '.join(ciphertext)

def main():
    # Read plaintext and RSA public key from standard input
    plaintext = input("Enter the ASCII string to encrypt: ").strip()
    e, n = map(int, input("Enter the values for e and n separated by a space: ").strip().split())

    # Encrypt the input string using the RSA algorithm
    encrypted_message = rsa_encrypt(plaintext, e, n)
    #print(f"Encrypted message: {encrypted_message}")

    # Convert the encrypted message back to ASCII characters
    decrypted_message = ''.join(chr(int(c)) for c in encrypted_message.split())
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
