n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

arr = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(n):
    for j in range(n):
        arr[i+1][j+1] = grid[i][j]

if k <= n:
    dir_idx = 0
    r, c = 0, k
elif k <= 2*n:
    dir_idx = 1
    r, c = k-n, n+1
elif k <= 3*n:
    dir_idx = 2
    r, c = n+1, 3*n+1-k
elif k <= 4*n:
    dir_idx = 3
    r, c = 4*n+1-k, 0

def in_range(nr, nc):
    return 0 < nr and nr < n+1 and 0 < nc and nc < n+1
    
nr = r + dr[dir_idx]
nc = c + dc[dir_idx]
cnt = 0

while(in_range(nr, nc)):
    
    if arr[nr][nc] == "\\":
        dir_idx = 3 - dir_idx

    elif arr[nr][nc] == "/":
        if dir_idx == 0:
            dir_idx = 1
        elif dir_idx == 1:
            dir_idx = 0
        elif dir_idx == 2:
            dir_idx = 3
        elif dir_idx == 3:
            dir_idx = 2

    nr = nr + dr[dir_idx]
    nc = nc + dc[dir_idx]
    cnt += 1
        
print(cnt)
