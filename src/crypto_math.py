# ------------------------------------------------------------
# src/crypto_math.py
# A class for the cryptography math I need for my projects
# 
# <diogopinto> 2025+
# ------------------------------------------------------------

class crypto_math:

    # EN: The Euclidean algorithm is a method for finding the greatest common divisor (GCD) of two integers,
    def gcd(val_a, val_b):

        # EN: If b > a switch values using tuple unpacking
        if (val_b > val_a): val_a, val_b = val_b, val_a

        if (val_b == 0): return val_a

        while True:
            remainder = val_a % val_b

            if (remainder == 0): return val_b
            
            # EN: Replace a with b and b with the remainder
            val_a, val_b = val_b, remainder

    # EN: The extended version not only finds the GCD but also provides coefficients x and y such that: ax+by=GCD(a,b)
    # a = public key; x = private key (modular inverse); b = ø(n);
    def extended_gcd(a, b):

        # EN: Base case
        if (a == 0):
            return b, 0, 1
        
        gcd, x1, y1 = crypto_math.extended_gcd(b % a, a)

        x = y1 - (b // a) * x1
        y = x1

        return gcd, x, y
    
    def modular_inverse(a, mod):
        
        # EN: # a*x + mod*y = gcd(a, mod)
        gcd, x, y = crypto_math.extended_gcd(a, mod)

        # EN: If the number aren't coprime there's no inverse
        if (gcd != 1):
            raise Exception("[crypto_math] Modular inverse does not exist!")
        else:
            # EN: % mod ensures this value is positive
            return x % mod 

    # EN: This function determines the totient of n by using ø(n) = (p - 1) (q - 1)
    def totient(p, q):
        return (p - 1) * (q - 1)

    