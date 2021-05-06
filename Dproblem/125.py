N=int(input())
A=list(map(int,input().split()))
min=1000000000
fmi=0
sum=0
for a in A:
    if a<0:
        fmi=fmi^1
    absa=abs(a)
    if absa<min:
        min=absa
    sum+=absa
if fmi==1:
    print(sum-min*2)
else:
    print(sum)