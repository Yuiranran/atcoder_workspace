N,C,K=map(int,input().split())
inT=[]
for i in range(N):
    t=int(input())
    inT.append(t)
cntB=0
cntP=1
inT.sort()
lT=inT[0]
for i in range(N-1):
    T=inT[i+1]
    if cntP>=C or T-lT>K:
        cntB+=1
        lT=T
        cntP=0
    cntP+=1

print(cntB+1)