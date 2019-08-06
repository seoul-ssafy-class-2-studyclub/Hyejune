
for t in range(10):
    N = int(input())
    base_list = list(map(int, input().split()))

    i = 1
    while True:
        if base_list[0]-i <= 0:
            break
        else:
            base_list.append(base_list[0]-i)
            base_list.pop(0)
            
        if not i % 8:
            i = 1
        else:    
            i += 1
    print('#' + str(N) + ' ')
    print(base_list)