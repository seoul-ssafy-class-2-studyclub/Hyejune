# # 시작점은 (0,0), 도착지점은 (H-1, W-1)

# D_horse = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
# D_monkey = [(1,0), (0,1), (-1,0), (0,-1)]

# K = int(input())

# W, H = map(int, input().split())


# board = [0] * H

# for i in range(H):
#     board[i] = list(map(int, input().split()))


# min_result = 999999
# memory = {}
# flag = 0
# def pour_monkey(k, i, j, chance):
#     global min_result
#     global flag
#     if flag == 1:
#         return
#     if i == H-1 and j == W-1:
#         if k < min_result:
#             min_result = k
#             flag = 1
#         return
#     if memory.get((i,j,k)) != None:
#         return
#     else:
#         if chance > 0:
#             # 여기 다시
#             for a in range(12):
#                 if a < 8:
#                     di, dj = D_horse[a]
#                     ri = i + di
#                     rj = j + dj
#                     if 0 <= ri < H and 0 <= rj < W:
#                         if board[ri][rj] == 1:
#                             continue
#                         memory[(ri, rj, k)] = True
#                         pour_monkey(k+1, ri, rj, chance -1)
#                 if a >= 8:
#                     di, dj = D_monkey[a-8]
#                     ri = i + di
#                     rj = j + dj
#                     if 0 <= ri < H and 0 <= rj < W:
#                         if board[ri][rj] == 1:
#                             continue
#                         memory[(ri, rj, k)] = True
#                         pour_monkey(k+1, ri, rj, chance)

#         else:
#             for a in range(4):
#                 di, dj = D_monkey[a]
#                 ri = i + di
#                 rj = j + dj 
#                 if 0 <= ri < H and 0 <= rj < W:
#                     if board[ri][rj] == 1:
#                         continue
#                     memory[(ri, rj, k)] = True
#                     pour_monkey(k+1, ri, rj, chance)


# pour_monkey(0, 0, 0, K)

# if min_result == 999999:
#     min_result = -1
# print(min_result)


# 시작점은 (0,0), 도착지점은 (H-1, W-1)




###########################################################################################################################################################################



# import sys
# sys.setrecursionlimit(2000000)

# D_horse = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
# D_monkey = [(1,0), (0,1), (-1,0), (0,-1)]

# K = int(input())

# W, H = map(int, input().split())


# board = [0] * H

# for i in range(H):
#     board[i] = list(map(int, input().split()))


# min_result = 999999
# memory = {}
# flag = 0
# def pour_monkey(k, i, j, chance):
#     global min_result
#     global flag
#     if flag == 1:
#         return
#     if i == H-1 and j == W-1:
#         if k < min_result:
#             min_result = k
#             flag = 1
#         return
#     if memory.get((i,j,chance)) != None:
#         return
#     else:
#         if chance > 0:
#             # 여기 다시
#             for a in range(12):
#                 if a < 8:
#                     di, dj = D_horse[a]
#                     ri = i + di
#                     rj = j + dj
#                     if 0 <= ri < H and 0 <= rj < W:
#                         if board[ri][rj] == 1:
#                             continue
#                         memory[(ri, rj, chance)] = True
#                         pour_monkey(k+1, ri, rj, chance -1)
#                 if a >= 8:
#                     di, dj = D_monkey[a-8]
#                     ri = i + di
#                     rj = j + dj
#                     if 0 <= ri < H and 0 <= rj < W:
#                         if board[ri][rj] == 1:
#                             continue
#                         memory[(ri, rj, chance)] = True
#                         pour_monkey(k+1, ri, rj, chance)

#         else:
#             for a in range(4):
#                 di, dj = D_monkey[a]
#                 ri = i + di
#                 rj = j + dj 
#                 if 0 <= ri < H and 0 <= rj < W:
#                     if board[ri][rj] == 1:
#                         continue
#                     memory[(ri, rj)] = True
#                     pour_monkey(k+1, ri, rj, chance)


# pour_monkey(0, 0, 0, K)

# if min_result == 999999:
#     min_result = -1

# print(min_result)

import collections

D_horse = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
D_monkey = [(1,0), (0,1), (-1,0), (0,-1)]

K = int(input())

W, H = map(int, input().split())


board = [0] * H

for i in range(H):
    board[i] = list(map(int, input().split()))


memory = {}
flag = 0
queue = collections.deque([(0,0,0,K)]) # i, j , num_jump, chance

while queue:
    
    temp_i, temp_j, num_jump, chance_left = queue.popleft()

    if temp_i == H-1 and temp_j == W - 1:
        flag = 1
        break

    if memory.get((temp_i, temp_j, chance_left)) != None:
        continue

    memory[(temp_i,temp_j,chance_left)] = True
    
    if chance_left > 0:
        # 여기 다시
        for a in range(12):
            if a < 8:
                di, dj = D_horse[a]
                ri = temp_i + di
                rj = temp_j + dj
                if 0 <= ri < H and 0 <= rj < W:
                    if board[ri][rj] != 1:
                        # memory[(ri, rj, chance_left)] = True
                        if memory.get((temp_i, temp_j, chance_left)) != None:
                            queue.append((ri, rj, num_jump + 1, chance_left - 1))
            if a >= 8:
                di, dj = D_monkey[a-8]
                ri = temp_i + di
                rj = temp_j + dj
                if 0 <= ri < H and 0 <= rj < W:
                    if board[ri][rj] != 1:
                        # memory[(ri, rj, chance_left)] = True
                        if memory.get((temp_i, temp_j, chance_left)) != None:
                            queue.append((ri, rj, num_jump + 1, chance_left))

    else:
        for a in range(4):
            di, dj = D_monkey[a]
            ri = temp_i + di
            rj = temp_j + dj 
            if 0 <= ri < H and 0 <= rj < W:
                if board[ri][rj] != 1:
                    # memory[(ri, rj, chance_left)] = True
                    if memory.get((temp_i, temp_j, chance_left)) != None:
                        queue.append((ri, rj, num_jump + 1, chance_left))

if flag == 1:
    print(num_jump)
else:
    print(-1)