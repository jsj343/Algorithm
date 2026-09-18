n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def isOne(arr, i, j):
    if arr[i][j] == 1:
        return 1
    else:
        return 0

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt = isOne(grid, i, j) + isOne(grid, i, j+1) + isOne(grid, i, j+2)
        max_cnt = max(max_cnt, cnt)

print(max_cnt)