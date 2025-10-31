# 🔐 RSA Implementation in Python

A basic implementation of the **RSA (Rivest–Shamir–Adleman) public-key cryptosystem** built in Python for educational purposes. This project includes functionality for key generation, encryption, and decryption. 

*Developed for my Applied Cryptography class*

---

## Features

* **Key Generation:** Generates 512-bit public and private RSA keys using two large random prime numbers.
* **Encryption:** Encrypts plaintext (converted to an integer) using the public key.
* **Decryption:** Decrypts ciphertext (an integer) back into plaintext using the private key.
* **Persistent Keys:** Automatically generates, saves and loads keys from `public.rsa` and `private.rsa` files.

---

## 🛠️ Setup and Installation

You need **Python 3** installed. This project also relies on the `sympy` library for prime number generation.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Di0go/rsa-implementation
    cd rsa-implementation/src
    ```

2.  **Install dependencies:**
    This project uses `sympy`. It's best practice to use a virtual environment.

    ```bash
    # Create and activate a virtual environment
    python3 -m venv venv
    source venv/bin/activate

    # Install the required library
    pip install sympy
    ```
3. **Run the main application file:**

    ```bash
    python3 rsa.py
    ```


---

## ⚠️ Known Limitations and Future Work

This implementation is for educational use only; **do not use it for secure, production-grade applications.**

* **Security Risk (Textbook RSA):** The code uses **raw exponentiation** without any standardized **padding** (like OAEP). This is known as "textbook RSA" and is fundamentally insecure against various attacks.

* **Message Size:** Encrypting the entire message as one integer is inefficient and limits the plaintext size to the key size (512 bits).

* **Key Storage:** Keys are currently stored as simple string representations of Python lists. **Future work** should implement **Base64** or **PEM encoding** for robust key persistence.