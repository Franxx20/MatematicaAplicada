import hashlib
from Crypto.Util.number import bytes_to_long

# The output of the hash function needs to be converted into a
# number that can be used with RSA math.

flag = "crypto{Immut4ble_m3ssag1ng}"


def encrypt():
    n = ""
    d = ""
    with open("./private.key", "r") as f:
        line = f.readline().split(" ")
        n = int(line[2])
        line = f.readline().split(" ")
        d = int(line[2])

    long_hash = bytes_to_long(hashlib.sha256(flag.encode("utf-8")).digest())

    print(f"{n}\n{d}")
    print(f"flag to long {flag}{long_hash}")
    c = pow(long_hash, d, n)
    print(f"hash encriptado {c}")


encrypt()
