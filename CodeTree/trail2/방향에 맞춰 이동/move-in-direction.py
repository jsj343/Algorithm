n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# W, S, N, E
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
pos = [0, 0]

for i in range(n):
    for _ in range(dist[i]):
        if dir[i] == 'W':
            pos[0] += dx[0]
            pos[1] += dy[0]
        
        elif dir[i] == 'S':
            pos[0] += dx[1]
            pos[1] += dy[1]

        elif dir[i] == 'N':
            pos[0] += dx[2]
            pos[1] += dy[2]

        elif dir[i] == 'E':
            pos[0] += dx[3]
            pos[1] += dy[3]

print(pos[0], pos[1])