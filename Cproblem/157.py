N,M=map(int,input().split())
s=[]
c=[]
minN=-1
f=False
for i in range(M):
    a,b=map(int,input().split())
    s.append(a)
    c.append(b)

for i in range(10**N):
    f=False
    if (int(i/(10**(N-1)))==0) and (N>1):
        continue
    for j in range(M):
        if c[j] != int((i/(10**(N-s[j])))%10):
            f=True
            break
    if f==True:
        continue
    if (minN>i) or (minN==-1):
        minN=i
print(minN)