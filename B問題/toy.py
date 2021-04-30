A,B,C=map(int,input().split())

m=998244353
a=A%m
b=B%m
c=C%m
ans=a*(a+1)//2*b*(b+1)//2*c*(c+1)//2
print(int(ans% m))
