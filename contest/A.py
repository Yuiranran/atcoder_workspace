S=input()
cnt=0
for i in range(len(S)-3):
    if S[i:i+4]=="ZONe":
        cnt+=1
print(cnt)