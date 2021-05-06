A,B,C=map(int,input().split())

m=998244353

ans=A*(A+1)//2*B*(B+1)//2*C*(C+1)//2
print(int(ans% 998244353))