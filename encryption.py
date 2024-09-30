from PIL import Image
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import os

# Function to pad the data to be a multiple of block size
def pad(data, block_size):
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([padding_len] * padding_len)
    return data + padding

# Load an image
input_image_path = r"C:\Desktop\sun\sunjpeg.jpeg"
image = Image.open(input_image_path)

# Convert image to bytes
image_bytes = image.tobytes()

# Generate a 24-byte key and an 8-byte IV
key = get_random_bytes(24)
iv = get_random_bytes(8)

# Create a Triple DES cipher object
cipher = DES3.new(key, DES3.MODE_CBC, iv)

# Pad and encrypt the image bytes
padded_image_bytes = pad(image_bytes, cipher.block_size)
encrypted_image_bytes = cipher.encrypt(padded_image_bytes)

# Save the encrypted image and key to files
encrypted_image_path = "C:\\Desktop\\sun\\encrypted_image.bin"
key_path = "C:\\Desktop\\sun\\key.bin"
iv_path = "C:\\Desktop\\sun\\iv.bin"

# Write the IV and encrypted image to a file
with open(encrypted_image_path, "wb") as f:
    f.write(iv)
    f.write(encrypted_image_bytes)

# Save the key to a file
with open(key_path, "wb") as f:
    f.write(key)

# Save the IV to a separate file
with open(iv_path, "wb") as f:
    f.write(iv)

print("Image encryption successful!")
