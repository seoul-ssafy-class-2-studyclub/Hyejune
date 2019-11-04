# BFS문제

# R/G/B 구분, RG/B 구분
D = [(0,1), (1,0), (-1,0), (0,-1)]
N = int(input())

board = [0]*N
board2 = [0]*N
for i in range(N):
    board[i] = list(input())

for i in range(N):
    board2[i] = board[i][:]
# print(board)


cnt_1 = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 'R' or board[i][j] == 'G' or board[i][j] == 'B':
            cnt_1 += 1
            queue = [(i,j)]
            temp_color = board[i][j]
            board[i][j] = cnt_1
            while queue:
                temp_i,temp_j = queue.pop(0)
                for l in range(4):
                    di, dj = D[l]
                    ri = temp_i + di
                    rj = temp_j + dj
                    if 0 <= ri < N and 0 <= rj < N:
                        if board[ri][rj] == temp_color:
                            board[ri][rj] = cnt_1
                            queue.append((ri,rj))

print(cnt_1, end=' ')

cnt_2 = 0
for i in range(N):
    for j in range(N):
        if board2[i][j] == 'R' or board2[i][j] == 'G' or board2[i][j] == 'B':
            cnt_2 += 1
            queue = [(i,j)]
            temp_color = board2[i][j]
            if temp_color == 'B':
                color_list = ['B']
            else:
                color_list = ['R','G']
            board2[i][j] = cnt_2
            while queue:
                temp_i,temp_j = queue.pop(0)
                for l in range(4):
                    di, dj = D[l]
                    ri = temp_i + di
                    rj = temp_j + dj
                    if 0 <= ri < N and 0 <= rj < N:
                        if board2[ri][rj] in color_list:
                            board2[ri][rj] = cnt_2
                            queue.append((ri,rj))

print(cnt_2)
