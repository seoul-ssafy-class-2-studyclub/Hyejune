for num in range(1, 11):
    base_list = []
    n = int(input())
    cnt = 0
    # for i in range(n):
    #     base_list.append([])

    for i in range(n):
        base_list.append(list(input().replace(' ','')))

    # print(base_list)

    # 첫줄에 2가 있는 경우 없앰
    for i in range(n):
        if base_list[0][i] == '2':
            base_list[0][i] = '0'

    # print(base_list)

    for i in range(n-1):
        for j in range(n):
            if base_list[i][j] == '0':
                if base_list[i+1][j] == '2':
                    base_list[i+1][j] = '0'

            if base_list[i][j] == '1':
                if base_list[i+1][j] == '2':
                    base_list[i][j] = '0'
                    base_list[i+1][j] = '0'
                    cnt += 1
                elif base_list[i+1][j] == '1':
                    base_list[i][j] = '0'
                elif base_list[i+1][j] == '0':
                    base_list[i][j] = '0'
                    base_list[i+1][j] = '1'

    print('#' + str(num) + ' ' + str(cnt))