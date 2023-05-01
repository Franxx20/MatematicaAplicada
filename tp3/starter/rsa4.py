p = 857504083339712752489993810777
q = 1029224947942998075080348647219

e = 65537


def prime_modular_multiplicative_inverse(e, p, q):
    return pow(e, -1, ((p - 1) * (q - 1)))


def main():
    print(
        "prime modular multiplative inverse ",
        f"{prime_modular_multiplicative_inverse(e,p,q)}",
    )


main()
