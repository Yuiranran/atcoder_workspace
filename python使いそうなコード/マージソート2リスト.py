
def marge_sort_double(list,sublist):
    l=len(list)
    if l<2:
        return [list,sublist]
    left=list[:(l+1)//2]
    right=list[(l+1)//2:]
    subleft=sublist[:(l+1)//2]
    subright=sublist[(l+1)//2:]
    left=marge_sort_double(left,subleft)
    right=marge_sort_double(right,subright)
    return marge_double(left,right)
 
def marge_double(left,right):
    list=[]
    sublist=[]
    lleft=len(left[0])
    lright=len(right[0])
    il=0
    ir=0
    while True:

        if right[0][ir]>left[0][il]:
            list.append(left[0][il])
            sublist.append(left[1][il])
            il+=1
            if il>=lleft:
                list=list+right[0][ir:]
                sublist=sublist+right[1][ir:]
                break
        else:
            list.append(right[0][ir])
            sublist.append(right[1][ir])
            ir+=1
            if ir>=lright:
                list=list+left[0][il:]
                sublist=sublist+left[1][il:]
                break
    return [list,sublist]
l=[1,5,2,3,4,9,1,2,0]
l2=[0,1,2,3,4,5,6,7,8]
print(marge_sort_double(l,l2))