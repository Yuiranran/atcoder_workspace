N=int(input())
A=list(map(int,input().split()))
cnt=0
for i in range(N):
    if A[i]==-1:
        continue
    if A[A[i]-1]-1==i:
        cnt+=1
        A[A[i]-1]=-1
print(cnt)