# D = [(0,1), (0,-1), (1,0), (-1,0)]

# M, N = map(int,input().split())

# board = [0 for i in range(N)]
# tomato_list = []

# total_num = 0
# for i in range(N):
#     board[i] = list(map(int,input().split()))
#     for j in range(M):
#         if board[i][j] == 1:
#             tomato_list.append([(i,j)])
#         if board[i][j] == 0:
#             total_num += 1

# # print(total_num)

# cnt = 0
# day = 0
# flag = 1

# if tomato_list == []:
#     flag = -1

# while True:
#     if flag == -1:
#         break
#     if cnt == total_num:
#         break
#     else:
#         for item in tomato_list:
#             if item == []:
#                 flag = -1
#                 continue
#             flag = 1
#             for __ in range(len(item)):
#                 temp_i, temp_j = item.pop(0)
#                 for i in range(4):
#                     di, dj = D[i]
#                     ri = temp_i + di
#                     rj = temp_j + dj
#                     if 0 <= ri < N and 0 <= rj < M:
#                         if board[ri][rj] == 0:
#                             # print((ri,rj))
#                             board[ri][rj] = 1
#                             item.append((ri,rj))
#                             cnt += 1
#         day +=1
#         # print(day)
            
# if flag == -1:
#     day = -1        

# print(day)

from collections import deque

D = [(0,1), (0,-1), (1,0), (-1,0)]

M, N = map(int,input().split())

board = [0 for i in range(N)]
tomato_list = deque()

total_num = 0
for i in range(N):
    board[i] = list(map(int,input().split()))
    for j in range(M):
        if board[i][j] == 1:
            tomato_list.append((i,j))
        if board[i][j] == 0:
            total_num += 1

# print(total_num)

cnt = 0
day = 0
flag = 1

if tomato_list == []:
    flag = -1

while True:
    if flag == -1:
        break
    if cnt == total_num:
        break
    else:
        if len(tomato_list) == 0:
            flag = -1
            break
        for __ in range(len(tomato_list)):
            temp_i, temp_j = tomato_list.popleft()
            for i in range(4):
                di, dj = D[i]
                ri = temp_i + di
                rj = temp_j + dj
                if 0 <= ri < N and 0 <= rj < M:
                    if board[ri][rj] == 0:
                        # print((ri,rj))
                        board[ri][rj] = 1
                        tomato_list.append((ri,rj))
                        cnt += 1
        day +=1
        # print(day)
            
if flag == -1:
    day = -1        

print(day)