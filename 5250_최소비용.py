# 다익스트라 알고리즘 적용 문제

# 이 방법으로 풀면 시간 초과
# test_num = int(input())
# D = [(0,1), (0,-1), (1,0), (-1,0)]
# for t in range(test_num):
#     N = int(input())
#     min_result = 999999
#     board = [0] * N
    
#     for i in range(N):
#         board[i] = list(map(int,input().split()))


#     def findWay(i,j,cost,visited):
#         global min_result
#         if i == N-1 and j == N-1:
#             if cost < min_result:
#                 min_result = cost
#             return
#         if cost >= min_result:
#             return
#         else:
#             temp_vis = [0] * N
#             for a in range(N):
#                 temp_vis[a] = visited[a][:]
#             temp_vis[i][j] = True
#             for a in range(4):
#                 di, dj = D[a]
#                 ri = i + di
#                 rj = j + dj
#                 # print(ri,rj)
#                 if 0 <= ri < N and 0 <= rj < N:
#                     if not temp_vis[ri][rj]:
#                         temp = 0
#                         if board[ri][rj] > board[i][j]:
#                             temp = board[ri][rj] - board[i][j]
#                         findWay(ri, rj, cost + 1 + temp, temp_vis)
    
#     findWay(0,0,0,[[False for j in range(N)] for i in range(N)])

#     print('#' + str(t+1) + ' ', end='')
#     print(min_result)
    


# 다익스트라 적용 - 아직도 느림()

# from pprint import pprint

# test_num = int(input())
# D = [(0,1), (0,-1), (1,0), (-1,0)]
# for t in range(test_num):
#     N = int(input())
#     min_result = 999999
#     board = [0] * N
    
#     for i in range(N):
#         board[i] = list(map(int,input().split()))

#     processed = [[False for j in range(N)] for i in range(N)]

#     distance = [[99999999 for j in range(N)] for i in range(N)]

#     distance[0][0] = 0

#     while True:
#         # pprint(distance)
        
#         current_i = -1
#         current_j = -1
#         min_dist = 99999999

#         if processed[N-1][N-1]:
#             break

#         for i in range(N):
#             for j in range(N):
#                 if (processed[i][j] == False) and distance[i][j] < min_dist:
#                     current_i = i
#                     current_j = j
#                     min_dist = distance[i][j]
        
#         # print(current_i, current_j)
#         processed[current_i][current_j] = True

#         for i in range(4):
#             di, dj = D[i]
#             ri = current_i + di
#             rj = current_j + dj
#             if 0 <= ri < N and 0 <= rj < N:
#                 temp = 0
#                 if board[ri][rj] > board[current_i][current_j]:
#                     temp = board[ri][rj] - board[current_i][current_j]
#                 if not processed[ri][rj] and distance[ri][rj] > min_dist + 1 + temp:
#                     distance[ri][rj] = min_dist + 1 + temp
            

#     print('#' + str(t+1) + ' ', end='')
#     print(distance[N-1][N-1])



# 힙큐 사용한 다익스트라 적용
from pprint import pprint
from heapq import heappop, heappush

test_num = int(input())
D = [(0,1), (0,-1), (1,0), (-1,0)]
for t in range(test_num):
    N = int(input())
    min_result = 999999
    board = [0] * N
    queue = []
    
    for i in range(N):
        board[i] = list(map(int,input().split()))

    distance = [[99999999 for j in range(N)] for i in range(N)]

    distance[0][0] = 0

    heappush(queue,(0,0,0))

    while queue:
        current_dist, current_i, current_j = heappop(queue)
        # print(current_dist, current_i, current_j)

        if current_dist > distance[current_i][current_j]:           # 여기 다시보기
            continue
        
        for i in range(4):
            di, dj = D[i]
            ri = current_i + di
            rj = current_j + dj

            if 0 <= ri < N and 0 <= rj < N:
                temp = current_dist + 1
                if board[ri][rj] > board[current_i][current_j]:
                    temp = current_dist + 1 + (board[ri][rj] - board[current_i][current_j])
                if distance[ri][rj] > temp:
                    distance[ri][rj] = temp
                    heappush(queue, (temp, ri, rj))

        if current_i == N-1 and current_j == N-1:
            break
                
    # print(distance)
    print('#' + str(t+1) + ' ', end='')
    print(distance[N-1][N-1])