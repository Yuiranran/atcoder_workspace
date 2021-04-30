import queue
N= int(input())
A=[0]
cnt=0
for i in range(N):
    a=int(input())
    max=cnt
    min=0
    while True:
        if cnt==0:
            cnt+=1
            A.append(a)
            max=cnt
            break
        ex=(max-min+1)//2+min
        q=A[ex]
        if q==a:
            A.pop(ex)
            cnt-=1
            break
        if q>a:
            if max==ex:
                A.insert(ex,a)
                cnt+=1
                break
            max=ex
        else:
            if max==ex:
                A.append(a)
                cnt+=1
                break
            min=ex
print(cnt)

