n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

arr = [[0 for _ in range(n)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(m):
    ans = 0
    r = points[i][0] - 1
    c = points[i][1] - 1
    arr[r][c] = 1
    cnt = 0

    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if in_range(nr, nc):
            if arr[nr][nc] == 1:
                cnt += 1

    if cnt == 3:
        ans = 1

    print(ans)