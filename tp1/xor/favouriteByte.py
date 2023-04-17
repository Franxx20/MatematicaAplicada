
import pwn
import time
def decipher():
    start_time = time.time()
    encription = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

    for i in range(0,255):
        #result = [chr(a ^ i) for a in encription]
        # result = pwn.xor(encription,i).decode('utf-8',errors = 'ignore')
        result = bytes.decode(pwn.xor(encription,i),"utf-8", errors = "ignore")

        flag = "".join(result)
        if(flag.startswith("crypto")):
            print(flag)
            print(f"{i} {chr(i)}")

    print(time.time() - start_time)


            

decipher()
