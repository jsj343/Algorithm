N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
dir_idx = 0

r, c = N//2, N//2
ans = board[r][c]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for i in range(T):
    if str[i] == 'L':
        dir_idx = (dir_idx -1 + 4) % 4

    elif str[i] == 'R':
        dir_idx = (dir_idx + 1) % 4

    elif str[i] == 'F':
        nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        if in_range(nr, nc):
            ans += board[nr][nc]
            r, c = nr, nc

print(ans)