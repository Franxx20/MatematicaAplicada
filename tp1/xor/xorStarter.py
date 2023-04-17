import pwn
import sys

def decipher():
    if(len(sys.argv) != 3):
        return "incorrect number of arguments"

    result = ""
    for c in str(sys.argv[1]):
        result+= chr(ord(c) ^int(sys.argv[2]))
        
    return f"crypto{{{result}}}"

    
def decipher2():
    if(len(sys.argv) != 3):
        return "incorrect number of arguments"

    result = (bytes.decode(pwn.xor(bytes(sys.argv[1],"utf-8"),int(sys.argv[2])),'utf-8'))
    return f"crypto{{{result}}}"



print(decipher())
print(decipher2())

