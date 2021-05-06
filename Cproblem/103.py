import math

N=int(input())
A=list(map(int, input().split()))
sum=0
lc=1
for i in range(N):
    lc=(lc * A[i]) // math.gcd(lc, A[i])
for i in range(N):
        sum+=(lc-1)%A[i]

print(sum)