n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# dir_num = 0(오른쪽), 1(아래쪽), 2(왼쪽), 3(위쪽)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir_num = 0
arr[0][0] = 1
num = 2
r, c = 0, 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for _ in range(n*m-1):

        nx, ny = r + dr[dir_num], c + dc[dir_num] 

        if in_range(nx, ny) and arr[nx][ny] == 0:
            pass

        else:
            dir_num = (dir_num + 1) % 4
            nx, ny = r + dr[dir_num], c + dc[dir_num]

        arr[nx][ny] = num
        num += 1
        r, c = nx, ny


for i in range(n):
    print(' '.join(map(str, arr[i])))


