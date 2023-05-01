def rsa_encrypt(number):
    exponent = 65537
    prime_1 = 17
    prime_2 = 23

    return (number**exponent) % (prime_1 * prime_2)


print(f"rsa_encryption of 12 = {rsa_encrypt(12)}")
