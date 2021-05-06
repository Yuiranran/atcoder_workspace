
#167
N,M=map(int,input().split())
k=[]
for i in range(M):
    l=list(map(int,input().split()))
    k.append(l)
p=list(map(int,input().split()))

ans=0
for i in range(2**N):
    cnt=[0]*M
    f=False
    for j in range(N):
        if ((i >> j) & 1):
            for ik,ok in enumerate(k):
                for iok,ook in enumerate(ok):
                    if iok==0:
                        continue
                    if ook == j+1:
                        cnt[ik]+=1
    for j in range(M):
        if cnt[j]%2 !=p[j]:
            f=True
    if f:
        continue
    ans+=1
    
print(ans)
