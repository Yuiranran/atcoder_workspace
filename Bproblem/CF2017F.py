S=input()
cnta=0
cntb=0
cntc=0

for i in S:
    if i=="a":
        cnta+=1
    if i=="b":
        cntb+=1
    if i=="c":
        cntc+=1
if (cnta-1)>cntb or (cnta-1)>cntc:
    exit(print("NO"))
if (cntb-1)>cnta or (cntb-1)>cntc:
    exit(print("NO"))
if (cntc-1)>cntb or (cntc-1)>cnta:
    exit(print("NO"))
print("YES")