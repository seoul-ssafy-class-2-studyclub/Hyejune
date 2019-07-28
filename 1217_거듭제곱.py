def recur_power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * recur_power(x, y - 1)

# print(recur_power(2, 5))

for t in range(10):
    n = int(input())
    base_list = list(map(int, input().split()))
    
    # a 의 b제곱 구하기
    a = base_list[0]
    b = base_list[1]

    print(f'#{t+1} {recur_power(a, b)}')
    
    