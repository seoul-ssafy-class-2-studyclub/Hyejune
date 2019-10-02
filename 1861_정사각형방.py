test_num = int(input())
D = [(0,1), (0,-1), (1,0), (-1,0)]

for t in range(test_num):
    N = int(input())
    board = [0] * N
    max_distance = -1
    result = -1
    for i in range(N):
        board[i] = list(map(int,input().split()))

    def my_func(x, y, temp):
        global max_distance
        global result
        for i in range(4):
            dx, dy = D[i]
            rx = x + dx
            ry = y + dy
            if 0 <= rx < N and 0 <= ry < N:
                if board[rx][ry] == board[x][y]+1:
                    my_func(rx, ry, temp+1)
                    
                else:
                    if temp > max_distance:
                        max_distance = temp
                        result = board[x][y] - temp
                        # return - 이거 쓰면 답 틀림
                    elif temp == max_distance and result > board[x][y] - temp:
                        result = board[x][y] - temp
                        # return - 이거 쓰면 답 틀림
            
            
    for i in range(N):
        for j in range(N):
            if result< board[i][j] <= result + max_distance:
                continue
            my_func(i, j, 0)

    print('#' + str(t+1) + ' ',end='')
    print(result, max_distance+1)   # 시작지점, 길이
    