N,T=map(int,input().split())
t=list(map(int,input().split()))
sum=0
for i in range(N-1):
    a=t[i+1]-t[i]
    if a>T:
        a=T
    sum+=a
print(sum+T)