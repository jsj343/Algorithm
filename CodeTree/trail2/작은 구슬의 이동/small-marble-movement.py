n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 상하의 dir_num 합 = 좌우의 dir_num 합 = 3 -> 현재 방향과 반대 방향으로 가려면 dir_num = (3 - dir_num)으로 변경
dir = {
    'U' : 2,
    'D' : 1,
    'R' : 0,
    'L' : 3
}

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

r_idx, c_idx = dir[d], dir[d]

for _ in range(t):
    x, y = r + dr[r_idx], c + dc[c_idx]

    if in_range(x, y):
        r, c = x, y
    else:
        r_idx, c_idx = 3 - r_idx, 3- c_idx

print(r, c)