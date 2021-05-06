def merge_sort(arr,b):
    if len(arr) <= 1:
        return [arr,b]

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]
    bleft = b[:mid]
    bright =b[mid:]
    

    # 再帰的に分割を行う
    L = merge_sort(left,bleft)
    R = merge_sort(right,bright)
    left=L[0]
    right=R[0]
    bleft=L[1]
    bright=R[1]

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right,bleft,bright)


def merge(left, right,bleft,bright):
    merged = []
    bmerged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            bmerged.append(bleft[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            bmerged.append(bright[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
        bmerged.extend(bleft[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
        bmerged.extend(bright[r_i:])
    return [merged,bmerged]
    
N,K=map(int,input().split())
A=[0]*N
B=[0]*N
cnt=0
for i in range(N):
    A[i],B[i]=map(int,input().split())
ans=merge_sort(A,B)
for i in range(N):
    cnt+=ans[1][i]
    if cnt>=K:
        exit(print(ans[0][i]))
