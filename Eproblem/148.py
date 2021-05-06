N=int(input())
if N%2==1 or N==0:
    exit(print(0))
cnt=0
i=5
while i <=N:
    cnt+=(N//i)//2
    i=i*5
print(cnt)