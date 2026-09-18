import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

total = 0
for i in range(n-1):
    total += abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])

min_dist = sys.maxsize

for i in range(1, n-1):
    dist = total - (abs(x[i+1]-x[i]) + abs(x[i]-x[i-1]) + abs(y[i+1]-y[i]) + abs(y[i]-y[i-1]))
    dist += abs(x[i+1]-x[i-1]) + abs(y[i+1]-y[i-1])
    min_dist = min(min_dist, dist)

print(min_dist)
