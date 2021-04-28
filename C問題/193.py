
N=int(input())
f=[False]*100001
i=2
cnt=0
while i*i<=N:
    if f[i]==True:
        i+=1
        continue
    j=2
    while True:
        ans=i**j
        if ans<=N:
            if ans*ans<=N:
                f[ans]=True
            cnt+=1
            j+=1
        else:
            break
    i+=1
print(N-cnt)