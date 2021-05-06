s=list(map(int,input().split()))
g=list(map(int,input().split()))

if (s[0]==g[0]) and (s[1]==g[1]):
    exit(print(0))
if s[0]+s[1]==g[0]+g[1]:
    exit(print(1))
if s[0]-s[1]==g[0]-g[1]:
    exit(print(1))
if abs(s[0]-g[0]) + abs(s[1]-g[1])<=3:
    exit(print(1))
if abs(s[0]-g[0]) + abs(s[1]-g[1])<=6:
    exit(print(2))
if (s[0]+s[1])%2==(g[0]+g[1])%2:
    exit(print(2))
for i in range(-3,4):
    for j in range(-3,4):
        if abs(i) + abs(j) >3:
            continue
        if s[0]+s[1]==(g[0]+i)+(g[1]+j):
            exit(print(2))
        if s[0]-s[1]==(g[0]+i)-(g[1]+j):
            exit(print(2))
        
print(3)