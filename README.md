# TripleDES-Image-Encryption
This repository provides Python scripts to encrypt and decrypt images using the Triple DES (3DES) encryption algorithm, a powerful method for securing data. The project includes separate scripts for image encryption and decryption, making it easy to protect and recover sensitive image files.


# TripleDES-Image-Encryption

This repository contains scripts for encrypting and decrypting images using the Triple DES (3DES) algorithm. The project demonstrates how to securely encrypt image data and subsequently decrypt it to retrieve the original image.

## Project Structure

- `encryption_script.py`: Python script to encrypt an image.
- `decryption_script.py`: Python script to decrypt an image.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Project documentation.

## Requirements

- Python 3.x
- Pillow
- pycryptodome

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/TripleDES-Image-Encryption.git
    ```

2. Navigate into the project directory:
    ```bash
    cd TripleDES-Image-Encryption
    ```

3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Encryption

1. Update the `input_image_path` in `encryption_script.py` to point to your image file.
2. Run the encryption script:
    ```bash
    python encryption_script.py
    ```
3. This will generate:
    - `encrypted_image.bin`: Encrypted image file.
    - `key.bin`: Encryption key.
    - `iv.bin`: Initialization vector.

### Decryption

1. Ensure the encrypted image, key, and IV files are correctly referenced in `decryption_script.py`.
2. Update `image_size` and `image_mode` in `decryption_script.py` to match your original image.
3. Run the decryption script:
    ```bash
    python decryption_script.py
    ```
4. The decrypted image will be saved as `decrypted_image.jpg`.
