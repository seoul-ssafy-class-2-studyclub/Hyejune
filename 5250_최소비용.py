test_num = int(input())
D = [(0,1), (0,-1), (1,0), (-1,0)]
for t in range(test_num):
    N = int(input())
    min_result = 999999
    board = [0] * N
    


    for i in range(N):
        board[i] = list(map(int,input().split()))


    def findWay(i,j,cost,visited):
        global min_result
        if i == N-1 and j == N-1:
            if cost < min_result:
                min_result = cost
            return
        if cost >= min_result:
            return
        else:
            temp_vis = [0] * N
            for a in range(N):
                temp_vis[a] = visited[a][:]
            temp_vis[i][j] = True
            for a in range(4):
                di, dj = D[a]
                ri = i + di
                rj = j + dj
                # print(ri,rj)
                if 0 <= ri < N and 0 <= rj < N:
                    if not temp_vis[ri][rj]:
                        temp = 0
                        if board[ri][rj] > board[i][j]:
                            temp = board[ri][rj] - board[i][j]
                        findWay(ri, rj, cost + 1 + temp, temp_vis)
    
    findWay(0,0,0,[[False for j in range(N)] for i in range(N)])

    print('#' + str(t+1) + ' ', end='')
    print(min_result)
    