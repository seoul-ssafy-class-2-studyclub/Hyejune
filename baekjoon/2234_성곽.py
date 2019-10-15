from pprint import pprint
D = [(0,-1), (-1,0), (0,1), (1,0)]  # 서, 북, 동, 남
N, M = map(int, input().split())

info_board = [0] * M
for i in range(M):
    info_board[i] = list(map(int, input().split()))

# pprint(info_board)

# def isAdj(num1, num2):
#     visited = [[False for j in range(N)] for i in range(M)]
#     for i in range(M):
#         for j in range(N):
#             if real_board[i][j] == num1:
#                 visited[i][j] = True
#                 for a in range(4):
#                     di, dj = D[i]
#                     ri = i + di
#                     rj = j + dj
#                     if 0 <= ri < M and 0 <= rj < N:
#                         if not visited[ri][rj]:
#                             visited[ri][rj] = True
#                             if real_board[ri][rj] == num2:
#                                 return True
#     return False
                        

adj = [set() for i in range(N*M + 1)]
real_board = [[0 for j in range(N)] for i in range(M)]
room_size = [0] * (M * N + 1)
max_size = 1
cnt = 0
for i in range(M):
    for j in range(N):
        if real_board[i][j] == 0:
            cnt += 1
            queue = [(i,j)]
            temp_size = 1
            while queue:
                temp_i, temp_j = queue.pop(0)
                real_board[temp_i][temp_j] = cnt
                # print(temp_i, temp_j)
                for a in range(4):
                    di, dj = D[a]
                    ri = temp_i + di
                    rj = temp_j + dj
                    if 0 <= ri < M and 0 <= rj < N:
                        if not info_board[temp_i][temp_j] & (1 << a):
                            if real_board[ri][rj] == 0:
                                real_board[ri][rj] = cnt
                                temp_size += 1
                                queue.append((ri,rj))
                        else:
                            if real_board[ri][rj] != 0 and real_board[ri][rj] != cnt:
                                adj[cnt].add(real_board[ri][rj])
                                
        room_size[cnt] = temp_size
        if temp_size > max_size:
            max_size = temp_size

# print(adj)

# max_comb = 2
# def comb(k, arr, temp_sum, now):
#     global max_comb
#     if k == 2:
#         if temp_sum > max_comb:
#             if arr[0] in adj[arr[1]]:
#                 max_comb = temp_sum
#     else:
#         for i in range(now + 1, cnt+1):
#             comb(k+1, arr + [i], temp_sum + room_size[i], i)
        
# comb(0, [], 0, 0)
max_sizes = 0
for nei in range(1, cnt + 1):
    if adj[nei]:
        for nxt in adj[nei]:
            temp = room_size[nei] + room_size[nxt]
            if temp > max_sizes:
                max_sizes = temp
# print(adj)                
# pprint(real_board)
print(cnt)
print(max_size)
print(max_sizes)