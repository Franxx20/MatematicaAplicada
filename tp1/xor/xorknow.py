import pwn

def decipher():
    encription= bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")


    
    #we know that the first 7 characters from the result are always crypto{
    #so we can take them as a base for the key we need
    partialKey = (bytes.decode(pwn.xor(encription[:7],b'crypto{'),'utf-8'))
    print(partialKey)
    #the result prints myXORke so we ASSUME all it lacks is a y. myXORkey and we use it a key
    totalKey = bytes((partialKey + "y"),'utf-8')


    #with the lastest key we try to get the result we want or keep guessing
    print(totalKey)
    print(bytes.decode(pwn.xor(encription,totalKey)))

        

decipher()
