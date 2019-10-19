from pprint import pprint

D = [(0,1), (1,0), (0,-1), (-1,0)]

N, M = map(int,input().split())

min_result = 9999
flag = -1
board = [0] * N
for i in range(N):
    board[i] = list(input())
    for j in range(M):
        if board[i][j] == 'B':
            B_idx = (i,j)
        elif board[i][j] == 'R':
            R_idx = (i,j)
        elif board[i][j] == 'O':
            end_idx = (i,j)

def movemove(R_i, R_j, B_i, B_j, cnt, vis):
    global flag
    for i in range(4):
        di, dj = D[i]
        ri = R_i + di
        rj = R_j + dj
        if board[ri][rj] == '#':
            continue
        if board[ri][rj] == 'O':
            min_result = cnt
            flag = 1
            return
        while True:
            if 
            ri += di
            rj += dj
            
            




visited = [[False for j in range(M)] for i in range(N)]
visited[R_idx[0]][R_idx[1]] = True
movemove(R_idx[0], R_idx[1], B_idx[0], B_idx[1], 0, visited)





