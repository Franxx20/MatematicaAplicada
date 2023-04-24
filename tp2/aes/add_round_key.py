from matrix import matrix2bytes
import pwn

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    xorMatrix = []

    for i in range(len(s)):
        row = []
        for j in range(len(s[i])):
            row.append(int.from_bytes(pwn.xor(s[i][j], k[i][j]), "big"))
        xorMatrix.append(row)

    return xorMatrix




result = add_round_key(state, round_key)
print(result)
print(matrix2bytes(add_round_key(state, round_key)))

