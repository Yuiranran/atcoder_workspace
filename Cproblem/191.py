H,W=map(int,input().split())
Map=""
for i in range(H):
    l=str(input())
    Map=Map+l
n=False
e=False
s=False
w=False
cnt=0
for i in range(1,H-1):
    w=False
    for j in range(1,W-1):
        if Map[i*W+j]==".":
            w=False
            continue
        if Map[(i-1)*W+j]=="#":
            if w:
                if Map[(i-1)*W+(j-1)]==".":
                    cnt+=1
            if Map[i*W+(j+1)]=="#":
                if Map[(i-1)*W+(j+1)]==".":
                    cnt+=1
        else:
            if not w:
                cnt+=1
            if Map[i*W+(j+1)]==".":
                cnt+=1
        if Map[i*W+(j+1)]=="#":
            if Map[(i+1)*W+j]=="#":
                if Map[(i+1)*W+(j+1)]==".":
                    cnt+=1
        else:
            if Map[(i+1)*W+j]==".":
                cnt+=1
        if Map[(i+1)*W+j]=="#":
            if w:
                if Map[(i+1)*W+(j-1)]==".":
                    cnt+=1
        else:
            if not w:
                cnt+=1
        w=True
print(cnt)        
