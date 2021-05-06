N=int(input())
A=list(map(int,input().split()))
B=[0]*(2**(N-1))
C=[i for i in range(2**N)]
j=1
while True:
    for i in range(2**(N-j)):
        if A[C[2*i]]>A[C[2*i+1]]:
            B[i]=C[2*i]
            ans=C[2*i+1]
        else:
            B[i]=C[2*i+1]
            ans=C[2*i]
    j+=1
    if j>=N+1:
        print(ans+1)
        break
    for i in range(2**(N-j)):
        if A[B[2*i]]>A[B[2*i+1]]:
            C[i]=B[2*i]
            ans=B[2*i+1]
        else:
            C[i]=B[2*i+1]
            ans=B[2*i]
    j+=1
    if j>=N+1:
        print(ans+1)
        break
