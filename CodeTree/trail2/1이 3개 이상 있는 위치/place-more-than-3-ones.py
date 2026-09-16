n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0

for r in range(n):
    for c in range(n):
        cnt = 0
        for i in range(4):
            x, y = r + dr[i], c + dc[i]
            if in_range(x, y) and grid[x][y] == 1: 
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)