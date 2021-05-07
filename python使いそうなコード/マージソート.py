
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
        if right[ir]>left[il]:
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
l=[1,5,2,3,4,9,1,2,0]
print(marge_sort(l))

