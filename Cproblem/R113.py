S=input()
cnt=0
alf=[0]*26
for i in range(len(S)-1,0,-1):
    if S[i]==S[i-1]:
        tmp=len(S)-1-i-(alf[ord(S[i])-ord('a')])
        if tmp>0:
            cnt+=tmp
        alf=[0]*26
        alf[ord(S[i])-ord('a')]+=len(S)-1-i
    alf[ord(S[i])-ord('a')]+=1
print(cnt)