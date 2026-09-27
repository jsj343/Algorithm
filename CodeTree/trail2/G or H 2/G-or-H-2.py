n = int(input())
people = [tuple(input().split()) for _ in range(n)]
people.sort(key = lambda x: int(x[0]))
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

ans = 0

# i: 구간의 시작점, j: 구간의 끝점, k: 구간 [i, j] 내 실질적 실행 위한 반복문
for i in range(n):
    for j in range(i, n):
        g_cnt, h_cnt = 0, 0
        conti_diff = 0
        for k in range(i, j+1):
            if alpha[k] == 'G':
                g_cnt += 1
            else:
                h_cnt += 1

            # 1. 같은 문자 연속인 경우
            if k != i:
                if alpha[k] == alpha[k-1]:
                    conti_diff += (pos[k]-pos[k-1])
                    ans = max(ans, conti_diff)
                else:
                    conti_diff = 0

        # 2. G와 H가 같은 개수인 경우
        if g_cnt == h_cnt:
            ans = max(ans, pos[j]-pos[i])

print(ans)
