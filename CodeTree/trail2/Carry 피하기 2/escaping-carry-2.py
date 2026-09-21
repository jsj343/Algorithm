import sys
n = int(input())
arr = [int(input()) for _ in range(n)]

lst = [[0 for _ in range(5)] for _ in range(n)]

# lst 안에 522 -> [0, 0, 5, 2, 2]로 분리해서 추가
for i in range(n):
    num = arr[i]
    idx = 4
    for j in range(5):
        num1 = num // (10**idx)
        num2 = num % (10**idx)
        lst[i][j] = num1
        num = num2
        idx -= 1

max_value = - 1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            flag = 0
            for l in range(5):
                if lst[i][l] + lst[j][l] + lst[k][l] >= 10:
                    flag = 1
            if flag == 0:
                value = arr[i] + arr[j] + arr[k]
                max_value = max(value, max_value)

print(max_value)
# for i in range(len(lst)):
#     print(lst[i])
