n, m = map(int, input().split())

arr= [[0 for _ in range(m)] for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

r, c= 0, 0
dir_idx = 0
num = 2

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            arr[0][0] = 1
            continue
        nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        if in_range(nr, nc) and arr[nr][nc] == 0:
            pass
        else:
            dir_idx = (dir_idx -1 + 4) % 4 
            nr, nc = r + dr[dir_idx], c + dc[dir_idx]
            
        arr[nr][nc] = num
        num += 1
        r, c = nr, nc
        
# map(arg1, arg2) : arg2(반복 가능한 객체)의 모든 요소들을 하나씩 꺼내어 arg1(함수)에 대입, 그 결과들을 모아서 돌려주는 역할
for i in range(n):
    print(' '.join(map(str, arr[i])))


