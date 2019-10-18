# 시간초과뜸

from pprint import pprint
from heapq import heappush, heappop
D = [(0,1), (0,-1), (1,0), (-1,0), (1, 1), (1,-1), (-1,1), (-1,-1)]


N, M, K = map(int, input().split())

board = [[[] for j in range(N)] for i in range(N)]

tree_food = [[5 for j in range(N)] for i in range(N)]

A = [0] * N

for i in range(N):              # 각 칸에 추가하는 양분 정보가 저장됨 보드
    A[i] = list(map(int, input().split()))

for i in range(M):
    x, y, age = map(int, input().split())
    board[x-1][y-1].append(age)

year = 0
current_tree_num = M        # 나무가 죽거나 생길때 바로바로 -1, +1 해준다

while year < K:

    # 봄 + 여름
    for i in range(N):
        for j in range(N):
            flag = 1
            temp_tree_list = []
            if board[i][j] == []:
                continue
            for _ in range(len(board[i][j])):   # 해당 땅에 있는 나무 그루수만큼 반복
                if flag == 1:
                    temp_tree = board[i][j].pop(0)            # 현재보고있는 나무의 나이
                    
                    temp_difference = tree_food[i][j] - temp_tree    # 해당 땅에 남은 영양분 - 지금보고있는 나무나이
                    if temp_difference >= 0:
                        tree_food[i][j] -= temp_tree
                        temp_tree_list.append(temp_tree + 1)   # 양분을 잘 먹고 살아남은 나무는 나이 + 1해서 임시리스트에 저장
                    else:
                        flag = -1   # 충분한 양분이 없어서 못먹고 죽는 경우
                        tree_food[i][j] += temp_tree//2
                        M -= 1              # 나무가 죽었음
                if flag == -1:
                    if board[i][j]:
                        temp_tree = board[i][j].pop()
                        tree_food[i][j] += temp_tree//2
                        M -= 1                  # 나무가 죽었음
            board[i][j] = temp_tree_list
            board[i][j].sort()

    # 가을 + 겨울
    for i in range(N):
        for j in range(N):
            tree_food[i][j] += A[i][j]
            if board[i][j] == []:
                continue
            for tree in board[i][j]:
                if tree % 5 == 0:
                    for a in range(8):
                        di, dj = D[a]
                        ri = i + di
                        rj = j + dj
                        if 0 <= ri < N and 0 <= rj < N:
                            board[ri][rj].insert(0,1)     # 나무가 생김
                            M += 1
    year += 1
    
if M < 0:
    M = 0

print(M)
                    