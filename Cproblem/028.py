lN=list(map(int,input().split()))
maxsum=[0]*4
for i in range(2**5):
    cnt=0
    sum=0
    for j in range(5):
        if ((i >> j) & 1): 
            cnt+=1
            if cnt>3:
                break
            sum+=lN[j]
    if cnt==3:
        maxsum[0]=sum
        for j in range(3):
            if maxsum[j+1]<maxsum[j]:
                t=maxsum[j+1]
                maxsum[j+1]=maxsum[j]
                maxsum[j]=t


print(maxsum[1])
        