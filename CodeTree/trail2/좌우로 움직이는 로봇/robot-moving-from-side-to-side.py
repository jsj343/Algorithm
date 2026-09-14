n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
A_pos = [0]
B_pos = [0]
a_idx = 0
b_idx = 0

for i in range(n):
    for j in range(t[i]):
        if d[i] == 'L':
            A_pos.append(A_pos[a_idx]-1)
            a_idx += 1
        elif d[i] == 'R':
            A_pos.append(A_pos[a_idx]+1)
            a_idx += 1

for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == 'L':
            B_pos.append(B_pos[b_idx]-1)
            b_idx += 1
        elif d_b[i] == 'R':
            B_pos.append(B_pos[b_idx]+1)
            b_idx += 1

# 한 로봇이 종료 후 같은 위치 계속 머무르는 경우 대비하여 다른 로봇과 배열 맞춰줌
if (len(A_pos) < len(B_pos)):
    for _ in range(len(B_pos)-len(A_pos)):
        A_pos.append(A_pos[len(A_pos)-1])
elif (len(A_pos) > len(B_pos)):
    for _ in range(len(A_pos)-len(B_pos)):
        B_pos.append(B_pos[len(B_pos)-1])

cnt = 0
last_sign = 0

for a, b in zip(A_pos, B_pos):
    # a가 더 오른쪽에 있으면 1, b가 더 오른쪽에 있으면 -1, 같은 데 있으면 0
    current_sign = (a>b)-(a<b)
    if last_sign != 0 and current_sign == 0:
        cnt += 1
    last_sign = current_sign

print(cnt)