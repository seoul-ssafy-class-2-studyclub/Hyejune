# from pprint import pprint

# D = [(0,1), (1,0), (0,-1), (-1,0)]

# N, M = map(int,input().split())

# min_result = 9999
# flag = -1
# board = [0] * N
# for i in range(N):
#     board[i] = list(input())
#     for j in range(M):
#         if board[i][j] == 'B':
#             B_idx = (i,j)
#         elif board[i][j] == 'R':
#             R_idx = (i,j)
#         elif board[i][j] == 'O':
#             end_idx = (i,j)

# # pprint(board)
# # print(B_idx, R_idx, end_idx)

# def movemove(R_i, R_j, B_i, B_j, n, vis):
#     global min_result
#     global flag
#     if flag == 1:
#         return
#     if R_i == end_idx[0] and R_j == end_idx[1]:
#         flag = 1
#         min_result = n
#         return
#     if B_i == end_idx[0] and B_j == end_idx[1]:
#         flag = 1
#         min_result = -1
#         return
#     for i in range(4):
#         di, dj = D[i]
#         R_ri = R_i + di
#         R_rj = R_j + dj
#         if R_ri == B_i and R_rj == B_j and board[B_i+di][B_j+dj] == '#':
#             continue
#         if vis[R_ri][R_rj]:
#             continue
#         if board[R_ri][R_rj] != '#':
#             v = [0] * N
#             for a in range(N):
#                 v[a] = vis[a][:]
#             v[R_ri][R_rj] = True
#             if board[B_i+di][B_j+dj] == '#':
#                 movemove(R_ri,R_rj, B_i, B_j, n+1, v )
#             else:
#                 movemove(R_ri,R_rj, B_i+di, B_j+dj, n+1, v )

    

# visited = [[False for j in range(M)] for i in range(N)]
# visited[R_idx[0]][R_idx[1]] = True
# movemove(R_idx[0], R_idx[1], B_idx[0], B_idx[1], 0, visited)

# print(min_result)




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

# pprint(board)
# print(B_idx, R_idx, end_idx)

def movemove(R_i, R_j, B_i, B_j, n, vis, pre1, pre2):
    global min_result
    global flag
    if flag == 1:
        return
    if R_i == end_idx[0] and R_j == end_idx[1]:
        flag = 1
        min_result = n
        return
    if B_i == end_idx[0] and B_j == end_idx[1]:
        flag = 1
        min_result = -1
        return
    for i in range(4):
        di, dj = D[i]
        R_ri = R_i + di
        R_rj = R_j + dj
        if R_ri == B_i and R_rj == B_j and board[B_i+di][B_j+dj] == '#':
            continue
        if vis[R_ri][R_rj]:
            continue
        if board[R_ri][R_rj] != '#':
            v = [0] * N
            for a in range(N):
                v[a] = vis[a][:]
            
            while True:
                if board[R_ri][R_rj] == '#':
                    break
                v[R_ri][R_rj] = True
                R_ri += di
                R_rj += dj
                
            R_ri -= di
            R_rj -= dj
            if board[B_i+di][B_j+dj] == '#':
                movemove(R_ri,R_rj, B_i, B_j, n+1, v )
            else:
                movemove(R_ri,R_rj, B_i+di, B_j+dj, n+1, v )

    

visited = [[False for j in range(M)] for i in range(N)]
visited[R_idx[0]][R_idx[1]] = True
movemove(R_idx[0], R_idx[1], B_idx[0], B_idx[1], 0, visited)

print(min_result)



