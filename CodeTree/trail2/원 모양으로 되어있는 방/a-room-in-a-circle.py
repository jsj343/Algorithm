import sys
n = int(input())
a = [int(input()) for _ in range(n)]

min_dist = sys.maxsize
for i in range(n):
    dist = 0
    idx = i
    weight = 1
    for _ in range(n-1):
        dist += a[(idx + 1) % n]*weight
        weight += 1
        idx = (idx + 1) % n
    min_dist = min(dist, min_dist)

print(min_dist)