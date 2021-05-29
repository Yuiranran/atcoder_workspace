def marge_sort_multi(list,ikey):
    l=len(list)
    if l<2:
        return list
    left=list[:(l+1)//2]
    right=list[(l+1)//2:]
    left=marge_sort_multi(left,ikey)
    right=marge_sort_multi(right,ikey)
    return marge_multi(left,right,ikey)
 
def marge_multi(left,right,ikey):
    list=[]
    lleft=len(left)
    lright=len(right)
    il=0
    ir=0
    while True:

        if right[ir][ikey]>=left[il][ikey]:
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
    
l=[[1,5,7,4],[5,5,4,3],[4,3,9,6],[7,2,0,3]]
print(marge_sort_multi(l,0))
print(marge_sort_multi(l,1))
print(marge_sort_multi(l,2))