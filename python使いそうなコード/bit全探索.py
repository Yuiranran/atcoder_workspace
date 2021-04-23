
#167
N,M,X=map(int,input().split())
CA=[]
bi=0
minMoney=-1
for i in range(N):
  CA.append(list(map(int,input().split())))

for i in range(2**N):
  money=0
  U=[0]*M
  bU=[False]*M
  nX=0
  for j in range(N):
    if ((i >> j) & 1): 
      money+=CA[j][0]  #金額の更新
      for k in range(M):
        U[k]+=CA[j][k+1]　#理解度の更新
        if U[k]>=X:
          bU[k]=True    #理解度の閾値チェック
  if bU.count(True)>=M:
    if (minMoney>money) or (minMoney==-1):
      minMoney=money　　#最小値更新
print(minMoney)
