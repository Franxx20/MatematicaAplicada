prime_1 = 857504083339712752489993810777
prime_2 = 1029224947942998075080348647219


def prime_euler_totient(prime_1, prime_2):
    return (prime_1 - 1) * (prime_2 - 1)


def main():
    print(
        "euler totient given two primes\n",
        f"{prime_1} and {prime_2} = {prime_euler_totient(prime_1,prime_2)}",
    )
