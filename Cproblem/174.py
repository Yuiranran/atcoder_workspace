K=int(input())
a=7
cnt=1
for i in range(K):
    if a%K == 0:
        exit(print(cnt))
    a=(10*a+7)%K
    cnt+=1
print(-1)