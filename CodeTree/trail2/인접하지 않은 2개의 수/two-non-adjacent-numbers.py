n = int(input())
numbers = list(map(int, input().split()))

max_value = 0
for i in range(n-2):
    for j in range(i+2, n):
        diff =abs(numbers[i] + numbers[j])
        max_value = max(max_value, diff)

print(max_value)