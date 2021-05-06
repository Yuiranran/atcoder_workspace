#TLE
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
 a, b = map(int, input().split())
 graph[a].append(b)
 graph[b].append(a)
 
# 頂点1からの最短距離
dist = [-1] * (n+1)
dist[0] = 0
cnt=-1
d = deque()
while -1 in dist:
    p=dist.index(-1)
    dist[p]=0
    d.append(p)
    cnt+=1
    while d:
        v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
    dist[i] = 0
    d.append(i)


print(cnt)