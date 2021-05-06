N=int(input())
a=[0,0,1]
mod=10007
for i in range(3,N):
    a.append((a[i-3]+a[i-2]+a[i-1])%mod)

print(a[N-1])