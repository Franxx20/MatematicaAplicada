N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932

p = 857504083339712752489993810777
q = 1029224947942998075080348647219


def prime_modular_multiplicative_inverse(e, p, q):
    return pow(e, -1, ((p - 1) * (q - 1)))


def rsa_decrypt(c):
    return pow(c, prime_modular_multiplicative_inverse(e, p, q), N)


def main():
    print(f"rsa_encryption of N = {rsa_decrypt(c)}")


main()
