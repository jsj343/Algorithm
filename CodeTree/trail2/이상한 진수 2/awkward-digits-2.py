a = input()
a = list(a)
flag = 0

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        flag = 1
        break
if flag == 0:
    a[len(a)-1] = '0'

a = ''.join(a)
ans = 0
for i in range(len(a)):
    ans += 2**(len(a)-1-i) * int(a[i])

print(ans)


