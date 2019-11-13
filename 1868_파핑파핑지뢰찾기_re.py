from pprint import pprint

D = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]  # 8방향 확인용

test_num = int(input())

for t in range(test_num):
    N = int(input())
    board = [0] * N
     
    for i in range(N):
        board[i] = list(input())

    result = 0
    num_mine = 0
    num_board = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                num_board[i][j] = '*'
                num_mine += 1
            elif board[i][j] == '.':
                cnt = 0
                for l in range(8):
                    di, dj = D[l]
                    ri = i + di
                    rj = j + dj
                    if 0 <= ri < N and 0 <= rj < N:
                        if board[ri][rj] == '*':
                            cnt += 1
                num_board[i][j] = cnt
    
    num_none_mine = N * N - num_mine

    click_cnt = 0
    temp_cnt = 0
    for i in range(N):
        for j in range(N):
            if num_board[i][j] == 0:
                click_cnt += 1
                num_board[i][j] = -click_cnt
                temp_cnt += 1
                queue = [(i,j)]
                while queue:
                    temp_i, temp_j = queue.pop(0)
                    for l in range(8):
                        di, dj = D[l]
                        ri = temp_i + di
                        rj = temp_j + dj
                        if 0 <= ri < N and 0 <= rj < N:
                            if num_board[ri][rj] > 0:
                                num_board[ri][rj] = -click_cnt
                                temp_cnt += 1
                            elif num_board[ri][rj] == 0:
                                num_board[ri][rj] = -click_cnt
                                temp_cnt += 1
                                queue.append((ri,rj))

    result = click_cnt + (num_none_mine - temp_cnt)
                        


    # pprint(num_board)

    print('#' + str(t+1) + ' ', end='' )
    print(result)