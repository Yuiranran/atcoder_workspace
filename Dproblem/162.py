N=int(input())
S=input()
sum=0
#最大値
for j in range(2,N):
    a=j-1
    b=N-j
    if a>b:
        sum+=a*b-b
    else:
        sum+=a*b-a

#かぶり除外
kaburi=0
cntR=0
cntG=0
cntB=0
for i in range(1,N+1):
    cnt=0
    for j in range(i+1,N+1):
        if S[i-1]==S[j-1]:
            kaburi+=N-j
            if j-i<=N-j:
                kaburi-=1
            kaburi+=j-i-1-cnt
            if (i+j)%2==0:
                kaburi-=1
                if S[(i+j)//2-1]==S[i-1]:
                    kaburi+=1
            kaburi+=i-1
            if i-1>=j-i:
                kaburi-=1
                if S[i-(j-i)-1]==S[i-1]:
                    kaburi+=1
            if S[i-1]=="R":
                kaburi-=cntR
            if S[i-1]=="G":
                kaburi-=cntG
            if S[i-1]=="B":
                kaburi-=cntB
            cnt+=1
    if S[i-1]=="R":
        cntR+=1
    if S[i-1]=="G":
        cntG+=1
    if S[i-1]=="B":
        cntB+=1
            
            
# 最遅コード
# ans=0
# for j in range(2,N):
#     for i in range(j-1,0,-1):
#         L=S[i-1]
#         for k in range(j+1,N+1):
#             R=S[k-1]
#             if j-i==k-j:
#                 continue
#             if S[j-1]==L or S[j-1]==R or L==R:
#                 kaburi+=1
#                 continue
#             ans+=1
print(sum-kaburi)


