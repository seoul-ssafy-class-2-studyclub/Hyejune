from pprint import pprint

test_num = int(input())

for t in range(test_num):
    N, K = map(int,input().split())
    board = [[0] for i in range(N)]
    new_board = [[[0] for i in range(N)] for j in range(N)]
    compare_list = [1]*K
    for i in range(N):
        board[i] = list(map(int,input().split()))

    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[j][-1-i]


    cnt = 0
    for i in range(N):
        for j in range(0,N-K+1):
            if board[i][j:j+K] == compare_list:
                if j == 0:
                    if board[i][j+K] == 1:
                        continue
                    cnt += 1
                elif j + K == N:
                    if board[i][j-1] == 1:
                        continue
                    cnt += 1
                else:
                    if board[i][j+K] != 1 and board[i][j-1] != 1:
                        cnt += 1
            if new_board[i][j:j+K] == compare_list:
                if j == 0:
                    if new_board[i][j+K] == 1:
                        continue
                    cnt += 1
                elif j + K == N:
                    if new_board[i][j-1] == 1:
                        continue
                    cnt += 1
                else:
                    if new_board[i][j+K] != 1 and new_board[i][j-1] != 1:
                        cnt += 1


    print('#' + str(t+1) + ' ', end='')
    print(cnt)