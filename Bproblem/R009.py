
B=list(map(str,input().split()))
N=int(input())
def leftBig(a,b):
    Arg=[str(a),str(b)]
    for i,arg in enumerate(Arg):
        act=""
        for k in arg:
            for j in range(0,10):
                if k==B[j]:
                    act+=str(j)
        Arg[i]=int(act)
    if Arg[0]>Arg[1]:
        return True
    else:
        return False

def marge_sort(list):
    l=len(list)
    if l<2:
        return list
    left=list[:(l+1)//2]
    right=list[(l+1)//2:]
    left=marge_sort(left)
    right=marge_sort(right)
    return marge(left,right)

def marge(left,right):
    list=[]
    lleft=len(left)
    lright=len(right)
    il=0
    ir=0
    while True:
        if leftBig(right[ir],left[il]):
            list.append(left[il])
            il+=1
            if il>=lleft:
                list=list+right[ir:]
                break
        else:
            list.append(right[ir])
            ir+=1
            if ir>=lright:
                list=list+left[il:]
                break
    return list

A=[]
for i in range(N):
    a=int(input())
    A.append(a)
ans=marge_sort(A)
for i in ans:
    print(i)