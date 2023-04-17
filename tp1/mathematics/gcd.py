def gdc(a,b):
    while b!=0:
        next = b
        b = a % b
        a = next
    return a

def gdcRec(a,b):
    return gdcRec(b%a,a) if a else b

print(gdc(12,8))
print(gdc(66528,52920))

