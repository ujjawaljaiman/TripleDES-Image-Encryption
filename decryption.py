from PIL import Image
from Crypto.Cipher import DES3

# Function to unpad the data after decryption
def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

# Paths for encrypted image, key and IV
encrypted_image_path = r"C:\Desktop\sun\encrypted_image.bin"
key_path = r"C:\Desktop\sun\key.bin"
iv_path = r"C:\Desktop\sun\iv.bin"

# Load the key from a file
with open(key_path, "rb") as f:
    key = f.read()

# Load the IV from a file
with open(iv_path, "rb") as f:
    iv = f.read()

# Read the encrypted image file
with open(encrypted_image_path, "rb") as f:
    iv_read = f.read(8)  # Read the IV
    encrypted_image_bytes = f.read()  # Read the encrypted image bytes

# Create a new cipher with the same key and IV
decipher = DES3.new(key, DES3.MODE_CBC, iv_read)

# Decrypt and unpad the data
decrypted_image_bytes = decipher.decrypt(encrypted_image_bytes)
unpadded_image_bytes = unpad(decrypted_image_bytes)

# Determine the image mode and size
# Assuming the original image was in RGB mode
image_mode = "RGB"

# Replace (width, height) with the actual dimensions of the image
image_size = (220,148)

# Create an image from the decrypted bytes
output_image_path = "C:\\Desktop\\sun\\decrypted_image.jpg"
image = Image.frombytes(image_mode, image_size, unpadded_image_bytes)
image.save(output_image_path)

print("Image decryption successful!")
