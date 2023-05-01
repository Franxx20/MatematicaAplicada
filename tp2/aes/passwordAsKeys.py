import requests
import hashlib
from Crypto.Cipher import AES

POSSIBLE_KEYS = []
BASE_URL = "http://aes.cryptohack.org/passwords_as_keys/"


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return str(e)

    return decrypted.hex()


def get_ciphertext():
    r = requests.get(f"{BASE_URL}/encrypt_flag")
    data = r.json()
    return data["ciphertext"]


def main():
    ciphertext = get_ciphertext()

    # Read all the possible keys
    with open("words.txt") as file:
        POSSIBLE_KEYS = file.readlines()

    for key_without_strip in POSSIBLE_KEYS:
        key = key_without_strip.strip()
        # hasheado la key que obtengo del archivo
        hash_key = hashlib.md5(key.encode()).digest()
        # lo paso a string hexadecimal
        hash_hex = hash_key.hex()

        pass_hex = decrypt(ciphertext, hash_hex)
        password = bytearray.fromhex(pass_hex).decode("utf-8", errors="ignore")
        if password.startswith("crypto{"):
            print(password)


main()
