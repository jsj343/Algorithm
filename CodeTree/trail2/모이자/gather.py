import sys

n = int(input())
A = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n):
    total = 0
    for j in range(n):
        total += A[j] * abs(j-i)
    ans = min(ans, total)

print(ans)
