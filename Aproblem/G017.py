N,P=map(int,input().split())
A=list(map(int,input().split()))
cnt1=0
cnt0=0
for i in range(N):
    if 1==A[i]%2:
        cnt1+=1
        A[i]=1
    if 0==A[i]%2:
        cnt0+=1
        A[i]=0
ans1=(2**cnt1)//2
if cnt1==0 and P==0:
    ans1=1
ans0=(2**cnt0)
print(int(ans1*ans0))