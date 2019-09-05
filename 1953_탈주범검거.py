change = {0:(0,1), 1:(0,-1), 2:(1,0), 3:(-1,0)}
d = {1:[(1,0), (-1,0), (0,1), (0,-1)], 
    2:[(1,0), (-1,0)], 
    3:[(0,1), (0,-1)], 
    4:[(-1,0), (0,1)], 
    5:[(1,0), (0,1)], 
    6:[(1,0), (0,-1)], 
    7:[(-1,0), (0,-1)]
}         # i,j 행,열 (세로, 가로)순서인거 주의
compliment = {(1,0):(-1,0), (-1,0):(1,0), (0,1):(0,-1), (0,-1):(0,1)}     # 튜플은 딕셔너리의 키값으로 들어갈 수 있다

test_num = int(input())

for t in range(test_num):
    result = 0
    N, M, R, C, L = map(int,input().split())
    board = [0]*N

    for i in range(N):
        board[i] = list(map(int,input().split()))
    
    visited = [[False for j in range(M)] for i in range(N)]
    
    time = 1
    cnt = 1
    queue = [(R,C)]
    visited[R][C] = True
    while queue:
        if time == L:
            break
        else:
            print('여기')
            time += 1
            for __ in range(len(queue)):
                i, j = queue.pop(0)
                for l in range(4):
                    di, dj = change[l]
                    ri = i + di
                    rj = j + dj
                    if 0 <= ri < N and 0 <= rj < M and board[ri][rj] != 0 and visited[ri][rj] == False:
                        visited[ri][rj] = True
                        for a, b in d[board[i][j]]:
                            if compliment[(a,b)] in d[board[ri][rj]]:
                                queue.append((ri,rj))
                                cnt += 1

    print('#' + str(t+1) + ' ', end='')
    print(cnt)