N, K = map(int, input().split())
basket = [0] * 101

for _ in range(N):
    num, pos = map(int, input().split())
    basket[pos] += num

ans = 0

if K < 51:
    for i in range(101-2*K):
        total = 0
        for j in range(i, i+2*K+1):
            total += basket[j]
        ans = max(ans, total)
else:
    for i in range(101):
        ans += basket[i]
        
print(ans)