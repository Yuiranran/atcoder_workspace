N,K=map(int,input().split())
A=list(map(int,input().split()))
sA=sorted(A,reverse=True)
mod=1000000000+7
cnt1=0
cnt2=0
cntsame=0
for i in range(1,N):
    if sA[i-1]>sA[i]:
        cnt2+=1+cntsame
        cntsame=0
    else:
        cntsame+=1
    cnt1+=cnt2
cnt3=0
for i in range(N):
    for j in range(i+1,N):
        if A[i]>A[j]:
            cnt3+=1
ans=cnt3*K%mod+cnt1*(K-1)*K//2%mod
print(ans%mod)