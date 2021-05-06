N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sA=[0]*(N+1)
sB=[0]*(M+1)
for i in range(N):
    sA[i+1]=sA[i]+A[i]
for i in range(M):
    sB[i+1]=sB[i]+B[i]

ap=0
bp=0
cnt=0
while True:
    if ap>N:
        break
    k=K-sA[ap]
    if k <0:
        break
    while True:
        if k-sB[M-bp]<0:
            bp+=1
            continue
        if cnt < ap+M-bp:
            cnt=ap+M-bp
        break
    ap+=1
print(cnt)