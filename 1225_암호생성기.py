
for t in range(10):
    N = int(input())
    base_list = list(map(int, input().split()))

    i = 1
    while True:
        if i % 5 == 0:
            K = 5
        else:
            K = i % 5

        if base_list[0]-K <= 0:
            # print(base_list)
            base_list.append(0)
            base_list.pop(0)
            break
        else:
            base_list.append(base_list[0]-K)
            base_list.pop(0)
        # print()
        # print(base_list)
        # print('i값은' + str(K))

        i += 1
        


    print('#' + str(N) + ' ', end='')
    print(' '.join(map(str,base_list)))