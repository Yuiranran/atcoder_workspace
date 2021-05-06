N=int(input())
S=[]
sum=0
for i in range(N):
    s=int(input())
    S.append(s)
    sum+=S[i]
if sum%10 != 0:
    exit(print(sum))
sS=sorted(S)
for  i in sS:
    if i %10 !=0:
        exit(print(sum-i))
print(0)