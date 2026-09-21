n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

ans = 0

for i in range(n):
    for j in range(n):
        cnt1 = 0
        lst = []
        if (j+2) < n:
            cnt1 += (arr[i][j] + arr[i][j+1] + arr[i][j+2])
            lst.append([i, j])
            lst.append([i, j+1])
            lst.append([i, j+2])

            for k in range(n):
                for l in range(n):
                    if in_range(k,l+2) and [k, l] not in lst and [k, l+1] not in lst and [k, l+2] not in lst:
                        cnt2 = cnt1 + (arr[k][l] + arr[k][l+1] + arr[k][l+2])
                        ans = max(ans, cnt2)
                        cnt2 = 0
        else:
            continue

print(ans)
