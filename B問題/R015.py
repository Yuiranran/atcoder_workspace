N=int(input())
cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0
cnt6=0
for i in range(N):
    M,m=map(float,input().split())    
    if M>=35:
        cnt1+=1
    if 30<=M<35:
        cnt2+=1
    if 25<=M<30:
        cnt3+=1
    if m>=25:
        cnt4+=1
    if m<0 and M>=0:
        cnt5+=1
    if M<0:
        cnt6+=1
    del m,M

print(str(cnt1),str(cnt2),str(cnt3),str(cnt4),str(cnt5),str(cnt6))