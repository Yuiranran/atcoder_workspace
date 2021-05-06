#10**12=5000兆
S=input()
K=int(input())
i=0
cnt=0
s='1'
while True:
    if i>=len(S):
        break
    if S[i]!='1':
        s=S[i]
        break
    cnt+=1
    i+=1
if K<=cnt:
    print(1)
else:
    print(s)

        
        