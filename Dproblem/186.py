N=int(input())
A=list(map(int,input().split()))
a=sorted(A)
sum=0
for i in range(N-1):
    d=abs(a[i]-a[i+1])
    sum+=(1+i)*d*(N-1-i)

print(sum)