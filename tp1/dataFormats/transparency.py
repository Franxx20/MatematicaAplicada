import hashlib
from Crypto.PublicKey import RSA

pem = open('transparency.pem', 'r').read()
print("pem")
print(pem)

key = RSA.importKey(pem).public_key()

der = key.exportKey(format='DER')
print("der")
print(der)

sha256 = hashlib.sha256(der)
print("")
print(sha256)

sha256_fingerprint = sha256.hexdigest()

print(f"Public Key SHA256: {sha256_fingerprint}")

# search censys.io for public key fingerprint to find the associated certificate
# https://censys.io/certificates?q=29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2
