arr = []
for i in range(19):
    arr.append(list(input().split()))

# (i, j)가 좌측 상단에서 시작하므로 오른쪽, 아래쪽, 오른쪽 아래 대각선, 왼쪽 아래 대각선 방향만 체크
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def isWinner():
    ans = 0

    for i in range(19):
        for j in range(19):
            if arr[i][j] == '0':
                continue
            color = arr[i][j]           
            cnt = 1
            for k in range(4):
                for l in range(1, 5):
                    nr, nc = i + dr[k] * l, j + dc[k] * l
                    if in_range(nr, nc) and arr[nr][nc] == color:
                        cnt += 1
                    else:
                        break
                    if cnt == 5:
                        a, b = i + dr[k] * 2 + 1, j + dc[k] * 2 + 1
                        return int(color), a, b
    return 0, 0, 0

color, a, b = isWinner()
print(color)
if a != 0 or b != 0:
    print(a, b)


#             if arr[i][j] == '1':
#                 ans = 1
#                 cnt = 1

#                 for k in range(4):
#                     points = [[i,j]]
#                     cnt = 1
#                     for l in range(1, 5):
#                         nr = i + dr[k] * l
#                         nc = j + dc[k] * l
#                         if in_range(nr, nc) and arr[nr][nc] == '1':
#                             cnt += 1
#                             points.append([nr, nc])
#                         if cnt == 5:
#                             return ans, points
#             elif arr[i][j] == '2':
#                 ans = 2
#                 cnt = 1

#                 for k in range(4):
#                     points = [[i,j]]
#                     cnt = 1
#                     for l in range(1, 5):
#                         nr = i + dr[k] * l
#                         nc = j + dc[k] * l
#                         if in_range(nr, nc) and arr[nr][nc] == '2':
#                             cnt += 1
#                             points.append([nr, nc])
#                         if cnt == 5:
#                             return ans, points

# ans, points = isWinner()
# points.sort()
# points[2][0] += 1
# points[2][1] += 1

# a, b = points[2][0], points[2][1]
# print(ans)
# print(a, b)