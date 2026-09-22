n, k = map(int, input().split())
x = []  # 위치
c = []  # 'G' or 'H'
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

last = max(x)
lst = [''] * (last+1)
for i in range(n):
    lst[x[i]] = c[i]

ans, total = 0, 0

if last <= k:
    for i in range(1, last+1):
        if lst[i] == 'G':
            total += 1
        elif lst[i] == 'H':
            total += 2
    ans = total

else:    
    for i in range(1, last-k+1):
        total = 0
        for j in range(i, i+k+1):
            if lst[j] == 'G':
                total += 1
            elif lst[j] == 'H':
                total += 2
        ans = max(ans, total)

print(ans)
    