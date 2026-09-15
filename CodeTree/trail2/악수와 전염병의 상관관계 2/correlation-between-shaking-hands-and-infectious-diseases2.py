N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes.sort(key = lambda x : x[0])

# [a, b] -> a: 감염 여부(0이면 음성, 1이면 양성), b: 남은 전염 횟수 
lst = [[0, 0] for _ in range(N+1)]
lst[P][0] = 1
lst[P][1] = K

for i in range(T):
    x = handshakes[i][1]
    y = handshakes[i][2]

    if lst[x][0] == 0 and lst[y][0] == 0:
        continue

    elif lst[x][0] == 1 and lst[y][0] == 1:
        if lst[x][1] != 0:
            lst[x][1] -= 1
        if lst[y][1] != 0: 
            lst[y][1] -= 1

    elif lst[x][0] == 1 and lst[y][0] == 0:
        if lst[x][1] > 0:
            lst[y][0] = 1
            lst[y][1] = K
            lst[x][1] -= 1
        
    elif lst[x][0] == 0 and lst[y][0] == 1:
        if lst[y][1] > 0:
            lst[x][0] = 1
            lst[x][1] = K
            lst[y][1] -= 1

ans = ''
for i in range(1, N+1):
    ans += str(lst[i][0])
print(ans)
        
