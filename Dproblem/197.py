import math
N=int(input())
p0=list(map(int,input().split()))
pN=list(map(int,input().split()))
r=math.sqrt((p0[0]-pN[0])**2+(p0[1]-pN[1])**2)
cosc=abs(p0[0]-pN[0])/r
sinc=abs(p0[1]-pN[1])/r
center=[(p0[0]+pN[0])/2,(p0[1]+pN[1])/2]
abssita=2*math.pi/N
if p0[0]>=pN[0]:
    if p0[1]>=pN[1]:
        abspx=(r/2)*(cosc*math.cos(abssita)-sinc*math.sin(abssita))
        abspy=(r/2)*(sinc*math.cos(abssita)+cosc*math.sin(abssita))
    else:
        abspx=(r/2)*(cosc*math.cos(abssita)+sinc*math.sin(abssita))
        abspy=(r/2)*(-sinc*math.cos(abssita)+cosc*math.sin(abssita))
else:
    if p0[1]>=pN[1]:
        abspx=(r/2)*(-cosc*math.cos(abssita)-sinc*math.sin(abssita))
        abspy=(r/2)*(sinc*math.cos(abssita)-cosc*math.sin(abssita))
    else:
        abspx=(r/2)*(-cosc*math.cos(abssita)+sinc*math.sin(abssita))
        abspy=(r/2)*(-sinc*math.cos(abssita)-cosc*math.sin(abssita))


print(str(abspx+center[0]),str(abspy+center[1]))

    

 