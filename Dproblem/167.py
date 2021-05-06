N,K =map(int,input().split())
A=list(map(int,input().split()))
R=[0]
p=0
l=0
for i in range(N):
    p=A[p]-1
    R.append(p)
for i in range(len(R)-1):
    if R[i] in R[i+1:]:
        p=i
        l=R[i+1:].index(R[i])+i+1
        break
if K<l:
    exit(print(R[K]+1))
K=K-p
K=K%(l-p)
print(R[p+K]+1)
