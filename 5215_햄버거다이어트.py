test_num = int(input())

for t in range(test_num):
    N, L = map(int, input().split())
    score_list = []
    kcal_list = []
    idx_list = []
    result = 0
    result_list = []
    for i in range(N):
        a, b = map(int, input().split())
        score_list.append(a)
        kcal_list.append(b)

    print(score_list, kcal_list)

    for i in range(1<<N):
        idx_list.append([])
        sum_kcal = 0
        for j in range(N):
            if i & (1<<j):
                idx_list[i].append(j)
                sum_kcal += kcal_list[j]
        if sum_kcal > 1000:
            idx_list[i] = 0

    for i in range(idx_list.count(0)):
        idx_list.remove(0)

    for i in range(len(idx_list)):
        sum = 0
        for j in range(len(idx_list[i])):
            sum += score_list[j]
        result_list.append(sum)



    print(idx_list)
    print(result_list)

    # for key, val in base_dict.items():



    # print('#' + str(t+1) + ' ', end = '')
    # print(result)