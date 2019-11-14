test_num = int(input())

for t in range(test_num):
    min_result = 999999

    N = int(input())

    board = [0] * N
    for i in range(N):
        board[i] = list(map(int, input().split()))

    temp_list = []
    temp_list2 = []
    def combi(k, arr, now, temp_result):
        if k == N/2:
            temp_list.append(temp_result)
            temp_list2.append(arr)
            return
        else:
            for i in range(now+1, N):
                if  k == 0:
                    combi(k+1, arr + [i], i, temp_result)
                else:
                    new_temp = temp_result
                    for num in arr:
                        new_temp += board[num][i]
                        new_temp += board[i][num]
                    combi(k+1, arr + [i], i, new_temp)

    combi(0, [], -1, 0)
    # print(temp_list)
    # print(temp_list2)
    for i in range(len(temp_list)//2):
        temp = abs(temp_list.pop()-temp_list.pop(0))
        if temp < min_result:
            min_result = temp

    print('#' + str(t+1) + ' ', end='')
    print(min_result)