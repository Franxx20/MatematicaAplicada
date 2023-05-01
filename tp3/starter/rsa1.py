print(f"{101}^{17} mod {22663} = {pow(101, 17, 22663)} ")


def modular_pow(base, exponent, module):
    if module == 1:
        return 0

    return (base**exponent) % module


print(f"{101}^{17} mod {22663} = {modular_pow(101, 17, 22663)} ")
