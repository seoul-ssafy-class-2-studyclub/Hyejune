to= [0] * 150
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    for j in range(a, b):
        to[j] += 1

result = max(to)
print(result)