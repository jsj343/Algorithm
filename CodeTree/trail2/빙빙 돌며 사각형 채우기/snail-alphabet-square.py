n, m = map(int, input().split())

arr = [['' for _ in range(m)] for _ in range(n)]

# dir_idx = 0(오른쪽), 1(아래쪽), 2(왼쪽), 3(위쪽)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir_idx = 0
idx = 0
r, c = 0, 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            # 'A'의 ASCII code = 65 ~ 'Z'의 ASCII code = 90
            arr[i][j] = chr(65 + (idx % 26))
            idx += 1
            continue
        nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        if in_range(nr, nc) and arr[nr][nc] == '':
            pass
        else:
            dir_idx = (dir_idx + 1) % 4
            nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        arr[nr][nc] = chr(65 + (idx % 26))
        idx += 1
        r, c = nr, nc

for i in range(n):
    print(' '.join(arr[i]))

