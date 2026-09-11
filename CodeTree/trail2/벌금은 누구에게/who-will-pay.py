N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# 인덱스 1 ~ N까지만 사용 (인덱스 = 학생 번호)
lst = [0 for _ in range(N+1)]
ans = -1

for i in range(M):
    lst[student[i]] += 1
    if lst[student[i]] == K:
        ans = student[i]
        break

print(ans)