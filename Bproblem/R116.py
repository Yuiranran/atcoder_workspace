N=int(input())
A=list(map(int,input().split()))
ans=0
mod=998244353
A.sort()
ex=0
for i in range(N-1,-1,-1):
    ans+=(A[i]*A[i])%mod
    ans+=A[i]*ex%mod
    ex=(A[i]+ex*2)%mod
print(ans%mod)

