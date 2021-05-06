from collections import deque
N,M=map(int,input().split())
#ルート
R=[[] for _ in range(N)]

for i in range(M):
    a,b=map(int,input().split())
    R[a-1].append(b-1)
    R[b-1].append(a-1)

q=deque()
q.append(0)
#ゴール
g=[-1]*N
g[0]=0
while q:
    p=q.popleft()
    lp=p+1
    #未ゴールを queueに，
    # g[]に1への最短パスのうち最も近いものを
    for i in R[p]:
        if g[i]==-1:
            q.append(i)
            g[i]=lp
print("Yes")
#1への最短パスのうち最も近いものを順に出力
for i in range(1,N):
    print(g[i])