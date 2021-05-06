S=input()

n=S[0]
cnt=0
for i in S[1:]:
    if i!=n:
        n=i
        cnt+=1
print(cnt)