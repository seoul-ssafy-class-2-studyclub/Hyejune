test_num = int(input())
d = [[0,1], [0,-1], [1,0], [-1,0]]
for t in range(test_num):
    N, K = map(int,input().split())
    max_len = 1
    board = [0] * N
    for i in range(N):
        board[i] = list(map(int,input().split()))
    peak = 0
    peak_idx = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > peak:
                peak = board[i][j]
                peak_idx = []
                peak_idx.append([i,j])
            elif board[i][j] == peak:
                peak_idx.append([i,j])

    result_list = []
    def longestWay(y, x, arr, l, chance):
        global max_len
        for i in range(4):
            current_num = arr[-1]
            ry = y + d[i][0]
            rx = x + d[i][1]
            if 0 <= ry < N and 0 <= rx < N:
                if board[ry][rx] < current_num:
                    longestWay(ry, rx, arr+[board[ry][rx]], l+1, chance)
                else:
                    if chance:
                        result_list.append([arr,l])
                    else:
                        if current_num > board[ry][rx] - K:
                            longestWay(ry, rx, arr+[current_num - 1], l+1, True)
        if l > max_len:
            print(arr)
            max_len = l
        
    for i in range(len(peak_idx)):
        a, b = peak_idx[i]
        longestWay(a,b, [board[a][b]],1,False)

    print('#' + str(t+1) + ' ',end='')
    print(max_len)