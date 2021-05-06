N=int(input())
S=[]
for i in range(N):
    a,b,c,d,e=map(int,input().split())
    S.append([a,b,c,d,e])

M=1000000000
m=0
while True:

    sum=(M-m)//2
    cnt=0
    for i in S:
        cnta=0
        cntb=0
        cntc=0
        cntd=0
        cnte=0
        if i[0]>sum:
            cnta+=1
        if i[1]>sum:
            cntb+=1
        if i[2]>sum:
            cntc+=1
        if i[3]>sum:
            cntd+=1
        if i[4]>sum:
            cnte+=1

        






