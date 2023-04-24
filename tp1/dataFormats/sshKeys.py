from Crypto.PublicKey import RSA

with open("./bruce_rsa.pub") as f:
    key = RSA.import_key(f.read())
    print(f"Bruce ssh public key module{key.n}")
