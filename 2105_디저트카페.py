test_num = int(input())



for t in range(test_num):
    N = int(input())
    max_result = 0

    board = [0] * N
    for i in range(N):
        board[i] = list(map(int, input().split()))

    def dessert_tour(k,i,j,arr,move1,move2,temp_result):
        global max_result

        if k == 4:
            # print('k == 4')
            if temp_result > max_result:
                max_result = temp_result
            return

        if k == 0:
            # print('k == 0')
            cnt = 0
            temp_i = i
            temp_j = j
            now_arr = arr[:]
            for l in range(N-j-1):
                cnt += 1
                temp_i += 1
                temp_j += 1
                if not(0 <= temp_i < N and 0 <= temp_j < N):
                    return
                if board[temp_i][temp_j] in now_arr:
                    return
                now_arr += [board[temp_i][temp_j]]

                dessert_tour(k+1, temp_i, temp_j, now_arr, cnt, move2, temp_result + cnt)
                
        elif k == 1:
            # print('k == 1')
            cnt = 0
            temp_i = i
            temp_j = j
            now_arr = arr[:]
            for l in range(N-i-1):
                cnt += 1
                temp_i += 1
                temp_j -= 1
                if not(0 <= temp_i < N and 0 <= temp_j < N):
                    return
                if board[temp_i][temp_j] in now_arr:
                    return
                now_arr += [board[temp_i][temp_j]]
                dessert_tour(k+1, temp_i, temp_j, now_arr, move1, cnt, temp_result + cnt)

        elif k == 2:
            # print('k == 2')
            temp_i = i
            temp_j = j
            now_arr = arr[:]
            for l in range(move1):
                temp_i -= 1
                temp_j -= 1
                if not(0 <= temp_i < N and 0 <= temp_j < N):
                    return
                if board[temp_i][temp_j] in now_arr:
                    return
                now_arr += [board[temp_i][temp_j]]
            dessert_tour(k+1, temp_i, temp_j, now_arr, move1, move2, temp_result + move1)

        elif k == 3:
            # print('k == 3')
            temp_i = i
            temp_j = j
            now_arr = arr[:]
            for l in range(move2-1):
                temp_i -= 1
                temp_j += 1
                if not(0 <= temp_i < N and 0 <= temp_j < N):
                    return
                if board[temp_i][temp_j] in now_arr:
                    return
                now_arr += [board[temp_i][temp_j]]
            dessert_tour(k+1, temp_i, temp_j, now_arr, move1, move2, temp_result + move2-1)

        
    for i in range(N-2):
        for j in range(1, N-1):
            dessert_tour(0,i,j,[board[i][j]],-1,-1,1)
            
    if max_result == 0:
        max_result = -1

    print('#' + str(t+1) + ' ', end='')
    print(max_result)





