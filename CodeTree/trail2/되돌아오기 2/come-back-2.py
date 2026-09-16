commands = input()

# dir_idx = 0(오른쪽), 1(아래쪽), 2(왼쪽), 3(위쪽)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dir_idx = 3
x, y = 0, 0
time = 0

for i in range(len(commands)):
    if commands[i] == 'F':
        x += dx[dir_idx]
        y += dy[dir_idx]
    elif commands[i] == 'L':
        dir_idx = (dir_idx - 1 + 4) % 4
    elif commands[i] == 'R':
        dir_idx = (dir_idx + 1) % 4
    time += 1

    if x == 0 and y == 0 :
        break

if x != 0 or y != 0:
    time = -1

print(time)