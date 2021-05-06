import math
import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
A,B=map(int,input().split())
ansgcd=math.gcd(A,B)
ansf=prime_factorize(ansgcd)
c = collections.Counter(ansf)
print(1+len(c.keys()))
