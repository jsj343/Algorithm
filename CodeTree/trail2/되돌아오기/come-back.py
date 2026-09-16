N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

def move(N):

    pos = [0, 0]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    time = 0

    for i in range(N):
        for _ in range(dist[i]):
            if dir[i] == 'N':
                pos[0] += dx[0]
                pos[1] += dy[0]

            elif dir[i] == 'S':
                pos[0] += dx[1]
                pos[1] += dy[1]

            elif dir[i] == 'W':
                pos[0] += dx[2]
                pos[1] += dy[2]

            elif dir[i] == 'E':
                pos[0] += dx[3]
                pos[1] += dy[3]
        
            time += 1

            if pos[0] == 0 and pos[1] == 0:
                return time

    if pos[0] != 0 or pos[1] != 0:
        time = -1
        return time

ans = move(N)
print(ans)



        
    

