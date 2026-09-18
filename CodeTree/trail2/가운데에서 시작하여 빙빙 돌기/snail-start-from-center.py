n = int(input())
grid = [[0] * n for _ in range(n)]
num = 1

# 오른쪽, 위쪽, 왼쪽, 아래쪽
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
dir_idx = 0
r, c = n//2, n//2
size = 1

def in_range(x, y, size):
    return n//2 - size <= x <= n//2 +size and n//2 - size <= y <= n//2 + size

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            grid[n//2][n//2] = num
            num += 1
            continue
            
        nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        if in_range(nr, nc, size) and grid[nr][nc] == 0:
            grid[nr][nc] = num
            num += 1

        else:
            temp_dir_idx = dir_idx
            dir_idx = (dir_idx + 1) % 4
            nr, nc = r + dr[dir_idx], c + dc[dir_idx]

            if grid[nr][nc] != 0:
                size += 1
                dir_idx = temp_dir_idx
                nr, nc = r + dr[dir_idx], c + dc[dir_idx]
            
            grid[nr][nc] = num
            num += 1

        r, c = nr, nc
        
for i in range(n):
    print(' '.join(map(str, grid[i])))
