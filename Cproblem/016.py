from collections import deque
N,M=map(int,input().split())
#ルート
R=[[] for _ in range(N)]

for i in range(M):
    a,b=map(int,input().split())
    R[a-1].append(b-1)
    R[b-1].append(a-1)

q=deque()
#ゴール
cntfri=[0]*N
for j in range(N):
    q.append(j)
    g=[-1]*N
    g[j]=0
    while q:
        p=q.popleft()
        lp=p
        #未ゴールを queueに，
        # g[]に1への最短パスのうち最も近いものを
        for i in R[p]:
            if g[i]==-1:
                if lp ==j:
                    q.append(i)
                    g[i]=lp
                else:
                    g[i]=lp
                    cntfri[j]+=1
#1への最短パスのうち最も近いものを順に出力
for i in range(0,N):
    print(cntfri[i])