n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
#  i : 구간의 시작점 인덱스 (n-k)~(n-1) -> k개 선택
for i in range(n-k+1):
    total = 0
    # j : 구간
    for j in range(i, i+k):
        total += arr[j]
    ans = max(ans, total)

print(ans)
