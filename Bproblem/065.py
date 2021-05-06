N=int(input())
A=[0]*N
for i in range(N):
    A[i]=int(input())
j=0
cnt=0
for i in range(N):
    if j == 1:
        exit(print(cnt))
    j=A[j]-1
    cnt+=1
print(-1)