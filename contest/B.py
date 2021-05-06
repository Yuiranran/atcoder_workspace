N,D,H=map(int,input().split())
B=[]
maxx=-1
for i in range(N):
    d,h=map(int,input().split())

    x=((D/d)*h-H)/((D/d)-1)
    if x>maxx:
        maxx=x
if maxx<0:
    maxx=0
print(maxx)