S=input()
T=[]
f=1
cnt=0
for i in S:
    if i =="R":
        f=f^1
        continue
    if f==1:
        if cnt>0:
            if T[cnt-1]==i:
                T.pop(cnt-1)
                cnt-=1
                continue
        T.append(i)
    else:
        if cnt>0:
            if T[0]==i:
                T.pop(0)
                cnt-=1
                continue
        T.insert(0,i)
    cnt+=1
if f==1:
    for i in range(cnt):
        print(T[i],end="")
else:
    for i in range(cnt-1,-1,-1):
        print(T[i],end="")

