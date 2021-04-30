A,B,W=map(int,input().split())
i=1
max=-1
min=-1
while True:
    m=W*1000/i
    if m<A:
        break
    elif m>B:
        pass
    else:
        if max<i or max==-1:
            max=i
        if min>i or min==-1:
            min=i
    i+=1
if min==-1:
    exit(print("UNSATISFIABLE "))    
print(min,max)