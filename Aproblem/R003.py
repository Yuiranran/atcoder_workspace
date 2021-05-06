N=int(input())
r=input()
sum=0
for i in range(N):
    if r[i]=="F":
        continue
    sum+=4-ord(r[i])+ord('A')
print(sum/N)