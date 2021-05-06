S=input()
l=len(S)
nico=[]
i=0
while i<l:
    if S[i]=="2":
        i+=1
        if i<l and S[i]=="5":
            cnt=1
            i+=1
            while i<l:
                if S[i]=="2":
                    i+=1
                    if i<l and S[i]=="5":
                        cnt+=1
                        i+=1
                        continue
                break
            nico.append(cnt)
    else:
        i+=1
ans=0
for i in nico:
    ans+=i*(i+1)//2
print(ans)