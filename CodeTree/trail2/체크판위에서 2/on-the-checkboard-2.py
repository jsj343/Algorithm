R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

start = grid[0][0]
end = grid[R-1][C-1]
cnt = 0

for i in range(1, R):
    for j in range(1, C):
        if grid[i][j] != start:
            for k in range(i+1, R-1):
                for l in range(j+1, C-1):
                    if grid[k][l] != grid[i][j] and grid[k][l] != end:
                        cnt += 1

print(cnt)