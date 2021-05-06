N,L=map(int,input().split())
MAP=[]
for i in range(L):
    inp=input()
    MAP.append(" "+inp+" ")
pLead=input()
for i in range(len(pLead)):
    if pLead[i]=="o":
        p=i+1

for i in range(L-1,-1,-1):
    if MAP[i][p-1]=="-":
        p=p-2
        continue
    if MAP[i][p+1]=="-":
        p=p+2
print((p+1)//2)