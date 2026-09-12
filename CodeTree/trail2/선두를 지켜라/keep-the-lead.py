n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# A가 총 이동한 시간과 B가 총 이동한 시간이 동일하게 주어짐을 가정(문제 제한 조건)
total_time = sum(t)


A_pos = [0]
B_pos = [0]
a_idx = 0
b_idx = 0

for i in range(n):
    for j in range(t[i]):
        A_pos.append(A_pos[a_idx]+v[i])
        a_idx += 1

for i in range(m):
    for j in range(t2[i]):
        B_pos.append(B_pos[b_idx]+v2[i])
        b_idx += 1

cnt = 0
last_sign = 0
for a, b in zip(A_pos, B_pos):
    current_sign = (a>b)-(a<b)  # A가 선두면 1, B가 선두면 -1, 같으면 0
    if current_sign != 0:
        if last_sign != 0 and current_sign != last_sign:
            cnt += 1
        last_sign = current_sign

print(cnt)
