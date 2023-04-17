import math
def extended_gcd(a,b):
    if a<b:
        a,b = b,a # reversing the orden given

    r1,r2 = a,b
    s1,s2 = 1,0
    t1,t2 = 0,1

    while r2 > 0:
    # the next line is just the computation for the gcd
        q,r = divmod(r1,r2)
        r1,r2 = r2,r

        #the next line is for the computation of the Bézout's identity
        s1,s2 = s2,s1 -q * s2
        t1,t2 = t2,t1 - q * t2

    print(f"GCD:{r1}, u:{t1}, v:{s1} ")



extended_gcd(26513,32321)

    
