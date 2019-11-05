# from pprint import pprint
# D = [(0,1), (1,0), (0,-1), (-1,0)]
# N, K = map(int, input().split())

# board = [[0 for j in range(N)] for i in range(N)]
# queue = []
# for i in range(K):
#     a, b = map(int, input().split())
#     board[b-1][a-1] = 1
#     queue.append((b-1,a-1))

# # pprint(board)
# # print(queue)

# def check():
#     # 문명이 한덩어리인지 확인하는 함수
#     flag = 0
#     check_board = [0] * N
#     for i in range(N):
#         check_board[i] = board[i][:]

#     for i in range(N):
#         for j in range(N):
#             if check_board[i][j] == 1:
#                 if flag == 0:
#                     flag = 1
#                     check_board[i][j] == -1
#                     q = [(i,j)]
#                     while q:
#                         t_i, t_j = q.pop(0)
#                         for k in range(4):
#                             di, dj = D[k]
#                             ri = t_i + di
#                             rj = t_j + dj
#                             if 0 <= ri < N and 0 <= rj < N:
#                                 if check_board[ri][rj] == 1:
#                                     check_board[ri][rj] = -1
#                                     q.append((ri,rj))
#                 elif flag == 1:
#                     return False
#     return True


# cnt = 0

# while queue:
#     cnt += 1
#     for i in range(len(queue)):
#         temp_i, temp_j = queue.pop(0)

#         for k in range(4):
#             di, dj = D[k]
#             ri = temp_i + di
#             rj = temp_j + dj
#             if 0 <= ri < N and 0 <= rj < N:
#                 if board[ri][rj] == 0:
#                     board[ri][rj] = 1
#                     queue.append((ri,rj))
#     # pprint(board)
#     # print()

#     if check():
#         break



# print(cnt)



from pprint import pprint
D = [(0,1), (1,0), (0,-1), (-1,0)]
N, K = map(int, input().split())

board = [[0 for j in range(N)] for i in range(N)]
queue = []
civil = 1
for i in range(K):
    numnum = civil
    a, b = map(int, input().split())
    temp_i = b-1
    temp_j = a-1
    for l in range(4):
        di, dj = D[l]
        ri = temp_i + di
        rj = temp_j + dj
        if 0 <= ri < N and 0 <= rj < N:
            if board[ri][rj] != 0:
                numnum = board[ri][rj]
                civil -= 1
                break

    board[temp_i][temp_j] = numnum
    civil += 1
    queue.append((b-1,a-1))

# print(civil)
# pprint(board)
cnt_set = set()
cnt = 0
while queue:
    cnt += 1
    for i in range(len(queue)):
        temp_i, temp_j = queue.pop(0)
        temp_civil = board[temp_i][temp_j]

        for k in range(4):
            di, dj = D[k]
            ri = temp_i + di
            rj = temp_j + dj
            if 0 <= ri < N and 0 <= rj < N:
                if board[ri][rj] == 0:
                    board[ri][rj] = temp_civil
                    queue.append((ri,rj))
                    for kk in range(4):
                        ddi, ddj = D[kk]
                        rri = ri + ddi
                        rrj = rj + ddj
                        if 0 <= rri < N and 0 <= rrj < N:
                            if board[rri][rrj] != 0 and board[rri][rrj] != temp_civil:
                                if not (temp_civil,board[rri][rrj]) in cnt_set:
                                    cnt_set.add((temp_civil,board[rri][rrj]))
                                    cnt_set.add((board[rri][rrj],temp_civil))
                elif board[ri][rj] != 0 and board[ri][rj] != temp_civil:
                    if not (temp_civil,board[ri][rj]) in cnt_set:
                        cnt_set.add((temp_civil,board[ri][rj]))
                        cnt_set.add((board[ri][rj],temp_civil))
    # pprint(board)
    # print()
    # print(cnt_set)
    if len(cnt_set) >= 2 * (civil - 2):
        break



print(cnt)