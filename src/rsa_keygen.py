# ------------------------------------------------------------
# src/rsa_keygen.py
# A class for generating rsa public and private keys
# 
# <diogopinto> 2025+
# ------------------------------------------------------------
from sympy import randprime
from crypto_math import crypto_math
import random

class rsa_keygen:

    def keygen(bits=512):
        # EN: Randomly select two prime numbers (2²⁵⁶) according to the bitsize
        p = randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))
        q = randprime(2 ** (bits // 2 - 1), 2 **( bits // 2))

        while p == q:
            q = randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))

        # EN: n ≈ 2²⁵⁶×2²⁵⁶ = 2⁵¹²
        n = p * q

        # EN: Calculate the totient, ø(n) , of n
        phi = crypto_math.totient(p, q)

        # EN: Common choice
        e = 65537

        public_key = [e, n]

        # EN: Calculate the private key using the modular inverse
        d = crypto_math.modular_inverse(e, phi)

        private_key = [d, n]

        return public_key, private_key
