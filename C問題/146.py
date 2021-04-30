A,B,X=map(int,input().split())
ans=0
max=1000000001
i=max//2
while True:
    j=i
    if A*i+B*len(str(i))<=X:
        ans=i
        i=i+(max-i)//2
        if i==j:
            break
    else:
        max=i
        i=ans+(i-ans)//2
        if i == ans:
            break
    
print(ans)
