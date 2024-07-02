from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


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
file_name = 'yaxyo.txt.enc'  # Replace with your actual file name

# Decrypt the file
decrypt_file(file_name, key)
