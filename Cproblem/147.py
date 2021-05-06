N=int(input())
A=[0]*(N*N*2)
for i in range(N):
    A[i*N*2]=int(input())
    for j in range(A[i*N*2]):
        A[i*N*2+2*j+1],A[i*N*2+2*j+2]=map(int,input().split())

maxcnt=0
for i in range(2**N):
    cnt=0
    f=False
    for j in range(N):
        if ((i >> j) & 1):
            cnt+=1
            for k in range(A[j*N*2]):
                if A[j*N*2+k*2+2]!=((i >> (A[j*N*2+k*2+1]-1)) & 1):
                    f=True
                    break
            if f:
                break
    
    if (not f) and (cnt>maxcnt):
        maxcnt=cnt
print(maxcnt)