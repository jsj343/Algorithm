n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(input()))

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

cnt = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            for k in range(8):
                nr1, nc1 = i + dr[k], j + dc[k]
                nr2, nc2 = i + dr[k] * 2, j + dc[k] * 2
                if in_range(nr1, nc1) and in_range(nr2, nc2) and arr[nr1][nc1] == 'E' and arr[nr2][nc2] == 'E':
                    cnt += 1

print(cnt) 
