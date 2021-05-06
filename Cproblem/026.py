def ex(L):
    if not L:
        return 1
    max=-1
    min=-1
    for i in L:
        a=ex(i)
        if a>max or max==-1:
            max=a
        if a<min or min==-1:
            min=a

    return min+max+1
        

N=int(input())
B=[[] for _ in range(N)]
for i in range(N-1):
    b=int(input())
    B[b-1].append(B[i+1])
ans=ex(B[0])
print(ans)


