B,C=map(int,input().split())
cnt=0
a=1
if B==0:
    a=0
    cnt+=1
c=C//2
c1=(C-1)//2
c2=(C-2)//2
if c2<0:
    c2=0
if B>0:
    if B<=c1:
        cnt+=B*2+1
    else:
        cnt+=(c1+1)*2+c-c1
    cnt+=c2*2+c1-c2
else:

    cnt+=(c1+a)*2+c-c1
    if -B<=c2:
        cnt+=(-B-a)*2+a
    else:
        cnt+=c2*2+c1-c2
print(cnt)