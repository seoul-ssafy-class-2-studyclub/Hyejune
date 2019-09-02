from pprint import pprint
test_num = int(input())

change = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)}
direction = {1:2, 2:1, 3:4, 4:3}

for t in range(test_num):
    N, M, K = map(int,input().split())
    board = [0]*N
    for i in range(N):
        board[i] = [[]for i in range(N)]
    queue = []
    for i in range(K):
        queue.append(list(map(int,input().split())))
    
    def move(y, x, n, d): # 세로, 가로, 미생물수, 방향   ==>    미생물 움직이는 함수
        dx, dy = change[d]
        rx = x + dx
        ry = y + dy
        if rx == 0 or rx == N-1 or ry == 0 or ry == N-1:
            d = direction[d]
        return [ry, rx, n, d]

    for i in range(M):
        temp = []
        for j in range(len(queue)):
            y, x, n, d = queue.pop(0)
            if board[y][x] == [] or board[y][x][0] ! = n:   # 이런경우는 이 전 차례에 자신이 사라졌다는말이므로 다음 for문으로 continue해준다.
                continue
            board[y][x].pop(0)
            y, x, n, d = move[y, x, n, d]
            if n == 0:
                continue
            board[y][x].append([n,d])

            if len(board[y][x]) > 1:
                temp.appned([x,y])
            
            queue.append(y,z,n,d)

        for j in range(len(temp)):
            



