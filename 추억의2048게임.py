from pprint import pprint
test_num = int(input())

for t in range(test_num):
    N, side = input().split()
    N = int(N)
    board = [[0] for i in range(N)]
    visited = [[False for i in range(N)] for j in range(N)]
    for i in range(N):
        board[i] = list(map(int,input().split()))

    new_board = [[[0] for i in range(N)] for j in range(N)]

    if side == 'up':              # 90도
        for i in range(N):
            for j in range(N):
                new_board[i][j] = board[j][-1-i]

    elif side == 'down':              # -90도
        for i in range(N):
            for j in range(N):
                new_board[i][j] = board[-1-j][i]

    elif side == 'right':
        for i in range(N):
            new_board[i] = list(reversed(board[i]))

    else:
        new_board = board

    # pprint(new_board)
    def noZero():
        for i in range(N):
            for j in range(N):
                if new_board[i][j] == 0:
                    new_board[i].pop(j)
                    new_board[i].append(0)

    noZero()

    for i in range(N):
        # cnt = 0
        for j in range(1,N):
            pre = new_board[i][j-1]
            now = new_board[i][j]
            if pre == 0:
                continue
            if now == 0:
                new_board[i].pop(j)
                new_board[i].append(0)
                now = new_board[i][j]
            if now == pre and visited[i][j-1] == False:
                new_board[i][j-1] = pre * 2
                new_board[i][j] = 0
                visited[i][j] = True
    
    noZero()   
    # pprint(new_board)

    print('#' + str(t+1))
    if side == 'up':              # 90도
        for i in range(N):
            for j in range(N):
                print(new_board[-1-j][i], end =' ')
            print()

    elif side == 'down':              # -90도
        for i in range(N):
            for j in range(N):
                print(new_board[j][-1-i], end = ' ')
            print()

    elif side == 'right':
        for i in range(N):
            new_board[i].reverse()
            for j in range(N):
                print(new_board[i][j], end = ' ')
            print()

    else:
        for i in range(N):
            for j in range(N):
                print(new_board[i][j], end = ' ')
            print()
            
                
    