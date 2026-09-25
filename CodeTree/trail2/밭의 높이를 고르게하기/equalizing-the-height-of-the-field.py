import sys
N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(N-T+1):
    total = 0
    for j in range(i, i+T):
        total += abs(arr[j]-H)
    ans = min(ans, total)

print(ans)
