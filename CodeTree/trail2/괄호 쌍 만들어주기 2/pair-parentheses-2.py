A = input()
i_lst = []
j_lst = []

for i in range(len(A)-1):
    if A[i] == '(' and A[i+1] == '(':
        i_lst.append(i)
    elif A[i] == ')' and A[i+1] == ')':
        j_lst.append(i)

cnt = 0
for i in i_lst:
    for j in j_lst:
        if j >= (i+2):
            cnt += 1

print(cnt)