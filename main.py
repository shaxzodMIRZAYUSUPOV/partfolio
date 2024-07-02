from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


def encrypt_file(file_name, key):
    # Read the plaintext from the file
    with open(file_name, 'rb') as file:
        plaintext = file.read()

    # Create a cipher object using the key
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    # Pad the plaintext to be a multiple of the block size
    padded_text = pad(plaintext, AES.block_size)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)

    # Encode the IV and ciphertext as base64 to store them as text
    iv_b64 = base64.b64encode(iv).decode('utf-8')
    ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')

    # Write the IV and ciphertext to the file
    with open(file_name + '.enc', 'w') as file:
        file.write(iv_b64 + '\n' + ciphertext_b64)

    print(f"{file_name} muvaffaqiyatli shifrladi!")


def decrypt_file(file_name, key):
    # Read the IV and ciphertext from the file
    with open(file_name, 'r') as file:
        iv_b64 = file.readline().strip()
        ciphertext_b64 = file.readline().strip()

    iv = base64.b64decode(iv_b64)
    ciphertext = base64.b64decode(ciphertext_b64)

    # Create a cipher object using the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    padded_text = cipher.decrypt(ciphertext)

    # Unpad the plaintext
    plaintext = unpad(padded_text, AES.block_size)

    # Write the plaintext to a new file
    with open(file_name.replace('.enc', '_decrypted.txt'), 'wb') as file:
        file.write(plaintext)

    print(f"{file_name} muvaffaqiyatli shifridan yechildi!")


# Define the key and file name
key = b'1234567890123456'  # 16 byte (128-bit) key for AES-128
file_name = 'yaxyo.txt'  # Replace with your actual file name

# Encrypt the file
encrypt_file(file_name, key)

# Decrypt the file (for testing)
decrypt_file(file_name + '.enc', key)
