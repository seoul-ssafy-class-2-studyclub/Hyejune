test_num = int(input())

for num in range(test_num):

    N, K = map(int, input().split())
    mid_list = []
    result_list = []
    # for i in range(N):
    #     mid_list.append([])

    max_len = int(0.5 * (N - 1) * N) + 1

    i = 0
    
    while N > i:
        for a in range(1 + i, max_len):
            mid_list.append([])
            mid_list[i].append()
        i += 1
    print(mid_list)
    for n in range(N):
        if sum(mid_list[n]) == K:
            result_list.append(mid_list)
    mid_list = []
            

    
    print(result_list)


    # print('#' + str(num + 1) + ' ', end='')
    # print(result)

