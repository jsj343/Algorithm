dirs = input()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_idx = 3
pos = [0, 0]

for i in range(len(dirs)):
    if dirs[i] == 'F':
        pos[0] += dx[dir_idx]
        pos[1] += dy[dir_idx]

    elif dirs[i] == 'L':
        dir_idx = (dir_idx -1 + 4) % 4

    elif dirs[i] == 'R':
        dir_idx = (dir_idx + 1) % 4

print(pos[0], pos[1])