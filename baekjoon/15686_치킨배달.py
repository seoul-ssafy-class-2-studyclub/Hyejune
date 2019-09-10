from pprint import pprint

d = [(1,0), (-1,0), (0,1), (0,-1)]

N, M = map(int,input().split())
board = [0]*N
for i in range(N):
    board[i] = list(map(int,input().split()))

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))


# pick_num = len(chicken) - M         # 버릴거

# def shortest_chicken(arr):          # 배열 집어넣으면 치킨거리 반환해주는 함수
#     total = 0
#     for item in home:
#         queue = [item]
#         cnt = 0
#         flag = -1
#         while queue:
#             if flag == 1:
#                 break
#             cnt += 1
#             for a in range(len(queue)):
#                 temp_i, temp_j = queue.pop(0)
#                 for b in range(4):
#                     di, dj = d[b]
#                     if 0 <= temp_i + di < N and 0 <= temp_j + dj < N:
#                         if arr[temp_i + di][temp_j + dj] == 0:
#                             queue.append((temp_i + di, temp_j + dj))
#                         elif arr[temp_i + di][temp_j + dj] == 2:
#                             total += cnt
#
#                             flag = 1
#     return total

min_num = 9999
def pick_chicken(k, arr, now):
    global min_num
    if k == M:
        temp_val = 0
        for h in home:
            min_min = 999
            i1, j1 = h
            for a in arr:
                i2, j2 = a
                temp_min = abs(i1-i2) + abs(j1-j2)
                if temp_min < min_min:
                    min_min = temp_min
            temp_val += min_min
        if temp_val < min_num:
            min_num = temp_val
        return
    else:
        for i in range(now+1, len(chicken)):
            pick_chicken(k+1,arr+[chicken[i]],i)

pick_chicken(0, [], -1)
print(min_num)

