
N=int(input())
S=[]
ans=1
for i in range(N):
    s=input()
    if s[0]=='A':
        pass
    else:
        ans+=2**(i+1)
print(ans)

