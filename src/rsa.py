# ----------------------------------------------
# rsa-implementation/src/rsa.py
#
# RSA implementation in Python
#
# Applied Cryptography Class
# <diogopinto> 2025+
# ----------------------------------------------

from rsa_keygen import rsa_keygen
import os

class rsa:

    @staticmethod
    def encrypt(plaintext, public_key):

        return pow(plaintext, public_key[0], public_key[1])

    @staticmethod
    def decrypt(ciphertext, private_key):
        
        return pow(ciphertext, private_key[0], private_key[1])

def main():

    if not os.path.exists('private.rsa') or not os.path.exists('public.rsa'):
            # EN: Generate default keys
            keys = rsa_keygen.keygen()

            with open('private.rsa', 'w') as private, open('public.rsa', 'w') as public:
                private.write(str(keys[1]))
                public.write(str(keys[0]))
    else:
        keys = []

        # EN: Get the keys from the public.rsa and private.rsa files
        with open('private.rsa', 'r') as private, open('public.rsa', 'r') as public:
                private_temp = private.read().split(", ")
                public_temp = public.read().split(", ")

                private = [int(private_temp[0].strip('[')), int(private_temp[1].strip(']'))]
                public = [int(public_temp[0].strip('[')), int(public_temp[1].strip(']'))]

                keys = [public, private]

    while True:
        print("\n==============================\n" +
              "1.) Encrypt\n" +
              "2.) Decrypt\n" +
              "3.) Generate keys\n" +
              "4.) Exit\n" +
              "==============================\n")
        user_choice = input("Select an option > ")

        match user_choice:
            case '1':
                plaintext = str(input("Input your plaintext > "))

                # EN: Encode the plaintext to bytes and then turn it into an int for it to be passed to the encrypt function
                encoded = int.from_bytes(plaintext.encode('utf-8'), byteorder='big')
                cipher = rsa.encrypt(encoded, keys[0])

                print("\nYour cipher is: " + str(rsa.encrypt(encoded, keys[0])))

            case '2':
                cipher = input("Input your rsa cipher > ")

                # EN: Input sanitization
                if (not cipher.isdigit()):
                    print("\n[SDES] Invalid input!")
                    continue

                # EN: Decrypt the cipher 
                result = rsa.decrypt(int(cipher), keys[1])

                # EN: Convert the decrypted integer into just enough bytes to hold it, then interpret those bytes as UTF-8 text.
                decoded = result.to_bytes((result.bit_length() + 7) // 8, byteorder='big').decode('utf-8', errors='ignore')
                print("\nYour plaintext is: " + decoded)

            case '3':
                keys = rsa_keygen.keygen()

                with open('private.rsa', 'w') as private, open('public.rsa', 'w') as public:
                    private.write(str(keys[1]))
                    public.write(str(keys[0]))

                print(f"[RSA] Public Key: {keys[0]}")
                print(f"[RSA] Private Key: {keys[1]}")

            case '4': 
                exit(0)

            case _:
                print("[SDES] Invalid choice!\n")
                continue


if __name__== "__main__":
    main()