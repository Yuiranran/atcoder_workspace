N=int(input())
NG=[0]*3
n=3
for i in range(3):
    NG[i]=int(input())
    if NG[i]>N:
        n-=1

cnt=0
num=0
NG=sorted(NG)
for i in NG:
    if i==N:
        exit(print("NO"))
if NG[0]==NG[1]-1==NG[2]-2 and n==3:
    exit(print("NO"))
for i in range(n):
    a=(NG[i]-num)//3
    b=(NG[i]-num)%3
    if b==0:
        b=1
    cnt+=a
    num=NG[i]-b
a=(N-num)//3
b=(N-num)%3
if b!=0:
    a+=1
cnt+=a
if cnt<=100:
    exit(print("YES"))

print("NO")

