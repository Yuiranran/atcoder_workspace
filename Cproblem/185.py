L=int(input())
ans=1
for i in range(11):
    ans=ans*(L-1-i)//(i+1)
print(int(ans))