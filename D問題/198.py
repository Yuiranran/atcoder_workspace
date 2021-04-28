S1=str(input())
S2=str(input())
S3=str(input())

lC=[-1]*10
lP=[-1]*26
cntP=0


for li in range(len(S1)):
    if lP[ord(S1[li])-ord('a')]==-1:
        if cntP>=10:
            exit(print("UNSOLVABLE"))
        lP[ord(S1[li])-ord('a')]=cntP
        cntP+=1
for li in range(len(S2)):
    if lP[ord(S2[li])-ord('a')]==-1:
        if cntP>=10:
            exit(print("UNSOLVABLE"))
        lP[ord(S2[li])-ord('a')]=cntP
        cntP+=1
for li in range(len(S3)):
    if lP[ord(S3[li])-ord('a')]==-1:
        if cntP>=10:
            exit(print("UNSOLVABLE"))
        lP[ord(S3[li])-ord('a')]=cntP
        cntP+=1

for a in range(10):
    for b in range(10):
        if b==a:
            continue
        for c in range(10):
            if (c==a) or (c==b):
                continue
            for d in range(10):
                if (d==a) or (d==b) or (d==c):
                    continue
                for e in range(10):
                    if (e==a) or (e==b) or (e==c) or (e==d):
                        continue
                    for f in range(10):
                        if (f==a) or (f==b) or (f==c) or (f==d) or (f==e):
                            continue
                        for g in range(10):
                            if (g==a) or (g==b) or (g==c) or (g==d) or (g==e) or (g==f):
                                continue
                            for h in range(10):
                                if (h==a) or (h==b) or (h==c) or (h==d) or (h==e) or (h==f) or (h==g):
                                    continue
                                for i in range(10):
                                    if (i==a) or (i==b) or (i==c) or (i==d) or (i==e) or (i==f) or (i==g) or (i==h):
                                        continue
                                    for j in range(10):
                                        if (j==a) or (j==b) or (j==c) or (j==d) or (j==e) or (j==f) or (j==g) or (j==h) or (j==i):
                                            continue
                                        lC[0]=str(a)
                                        lC[1]=str(b)
                                        lC[2]=str(c)
                                        lC[3]=str(d)
                                        lC[4]=str(e)
                                        lC[5]=str(f)
                                        lC[6]=str(g)
                                        lC[7]=str(h)
                                        lC[8]=str(i)
                                        lC[9]=str(j)
                                        if (lC[lP[ord(S1[0])-ord('a')]]=="0") or (lC[lP[ord(S2[0])-ord('a')]]=="0") or (lC[lP[ord(S3[0])-ord('a')]]=="0"):
                                            continue
                                        N1=""
                                        N2=""
                                        N3=""
                                        for li in range(len(S1)):
                                            N1=N1+lC[lP[ord(S1[li])-ord('a')]]
                                        for li in range(len(S2)):
                                            N2=N2+lC[lP[ord(S2[li])-ord('a')]]
                                        for li in range(len(S3)):
                                            N3=N3+lC[lP[ord(S3[li])-ord('a')]]
                                        if int(N1)+int(N2)==int(N3):
                                            print(N1)
                                            print(N2)
                                            print(N3)
                                            exit()
print("UNSOLVABLE")                                            