N,M=map(int,input().split())
if N==1 and M==1:
    exit(print(1))
if N==1:
    exit(print(M-2))
if M==1:
    exit(print(N-2))
print(N*M-(2*N+2*M-4))