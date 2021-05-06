from collections import deque

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
q = deque()
y= deque()
inA=0
for i in range(M):
    iq=0
    iy=0
    iA=0
    if len(q)>0:
        iq=q[0]
    if len(y)>0:
        iy=y[0]
    if len(A)>inA:
        iA=A[inA]
    if iA>=iq and iA>=iy:
        inA+=1
        q.append(iA//2)
    else:
        if iy>iA and iy>=iq:
            tmp=y.popleft()
            q.append(tmp//2)
        elif iq>iA and iq>iy:
            tmp=q.popleft()
            q.append(tmp//2)
        if len(A)>inA:
            y.append(iA)
            inA+=1
sum=0
while inA<len(A):
    sum+=A[inA]
    inA+=1
while y:
    sum+=y.popleft()
while q:
    sum+=q.popleft()

print(sum)