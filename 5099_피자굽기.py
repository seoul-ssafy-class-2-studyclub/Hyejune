test_num = int(input())

for t in range(test_num):
    N, M = map(int, input().split())

    cheese = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        pizza.append([i+1, cheese[i]])

    oven = pizza[0:N]
    rest = pizza[N:]

    while oven:
        if oven.count([]) == N-1:
            break
        for i in range(N):
            if oven[i] == []:
                continue
            oven[i][1] = oven[i][1]//2
            if oven[i][1] == 0:
                if rest == []:
                    oven[i] = []
                    if oven.count([]) == N-1:
                        break
                else:    
                    oven[i] = rest.pop(0)
            if oven.count([]) == N-1:
                break
    
    print('#' + str(t+1) + ' ', end='')
    for item in oven:
        if item != []:
            print(item[0])
    
    

