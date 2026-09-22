n = int(input())
arr = list(map(int, input().split()))

cnt = 0

# i: 구간의 시작 인덱스, j: 구간의 끝 인덱스, k: 구간 합 누적 계산용
for i in range(n):
    for j in range(i, n):
        total, avg = 0, 0
        interval = []
        for k in range(i, j+1):
            total += arr[k]
            interval.append(arr[k])
        avg = total / (j-i+1)
        for l in range(j-i+1):
            if interval[l] == avg:
                cnt += 1
                break

print(cnt)
