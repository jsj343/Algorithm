N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

if N >= M:
    for i in range(N-M+1):
        B_copy = B.copy()
        lst = []      
        for j in range(i, i+M):
            for k in range(len(B_copy)):
                if A[j] == B_copy[k]:
                    B_copy.remove(A[j])
                    lst.append(A[j])
                    break
            if len(B_copy) == 0:
                ans += 1

else:
    pass

print(ans)