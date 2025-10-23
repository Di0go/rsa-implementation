# ------------------------------------------------------------
# src/rsa_keygen.py
# A class for generating rsa public and private keys
# 
# <diogopinto> 2025+
# ------------------------------------------------------------
from crypto_math import crypto_math

class rsa_keygen:

    def keygen():
        # EN: Randomly select two prime numbers (in a real environment in a scale of 10¹⁰⁰)
        # TODO: Make these values random from a list of prime numbers
        p = 1543
        q = 7817

        n = p * q

        # EN: Calculate the totient, ø(n) , of n
        phi = crypto_math.totient(p, q)

        # EN: Get the public key (e), 1 < e < phi && gcd(e, phi) = 1
        e = 2
        while crypto_math.gcd(e, phi) != 1:
            e += 1

        public_key = [e, n]

        # EN: Calculate the private key using the modular inverse
        d = crypto_math.modular_inverse(e, phi)

        private_key = [d, n]

        return public_key, private_key

keys = rsa_keygen.keygen()
print(f"[RSA] Public Key: {keys[0]}")
print(f"[RSA] Private Key: {keys[1]}")