n = int(input())
S = input()

c_lst = []
o_lst = []
w_lst = []

for i in range(n):
    if S[i] == 'C':
        c_lst.append(i)

    elif S[i] == 'O':
        o_lst.append(i)

    elif S[i] == 'W':
        w_lst.append(i)

cnt = 0
for c in c_lst:
    for o in o_lst:
        for w in w_lst:
            if c < o < w:
                cnt += 1

print(cnt) 