import collections
n=int(input())
v=list(map(int,input().split()))
v0=[]
v1=[]
for i in range(n//2):
    v0.append(v[2*i])
    v1.append(v[2*i+1])
if n%2==1:
    v0.append(v[n-1])


cnt0=collections.Counter(v0)
numcnt0=cnt0.values()
maxnumcnt0=max(numcnt0)
keycnt0=list(cnt0.keys())
lnumcnt0=list(numcnt0)
maxcnt0=keycnt0[lnumcnt0.index(maxnumcnt0)]

cnt1=collections.Counter(v1)
numcnt1=cnt1.values()
maxnumcnt1=max(numcnt1)
keycnt1=list(cnt1.keys())
lnumcnt1=list(numcnt1)
maxcnt1=keycnt1[lnumcnt1.index(maxnumcnt1)]


if maxcnt0==maxcnt1:
    if maxnumcnt1>maxnumcnt0:
        tmp=0
        itmp=-1
        for i in range(len(lnumcnt0)):
            if keycnt0[i]==maxcnt0:
                continue
            if lnumcnt0[i]>tmp:
                tmp=lnumcnt0[i]
                itmp=i
    elif maxnumcnt0>maxnumcnt1:
        tmp=0
        itmp=-1
        for i in range(len(lnumcnt1)):
            if keycnt1[i]==maxcnt1:
                continue
            if lnumcnt1[i]>tmp:
                tmp=lnumcnt1[i]
                itmp=i
    else:
        tmp=0
        itmp=-1
        for i in range(len(lnumcnt0)):
            if keycnt0[i]==maxcnt0:
                continue
            if lnumcnt0[i]>tmp:
                tmp=lnumcnt0[i]
                itmp=i
        tmp1=0
        itmp1=-1
        for i in range(len(lnumcnt1)):
            if keycnt1[i]==maxcnt1:
                continue
            if lnumcnt1[i]>tmp1:
                tmp1=lnumcnt1[i]
                itmp1=i
        if tmp1>tmp:
            tmp=tmp1
    maxnumcnt1=tmp
print(n-(maxnumcnt1+maxnumcnt0))