from collections import deque

from pprint import pprint

D = [(1,0), (0,1), (0,-1), (-1,0)]

test_num = int(input())
for t in range(test_num):
    M, N, K = map(int,input().split())
    cnt = 0
    board = [[0 for j in range(M)] for i in range(N)]
    for i in range(K):
        b, a = map(int, input().split())
        board[a][b] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
                queue = deque()
                queue.append((i,j))
                while queue:
                    temp_i, temp_j = queue.popleft()
                    board[temp_i][temp_j] = -cnt

                    for a in range(4):
                        di, dj = D[a]
                        ri = temp_i + di
                        rj = temp_j + dj
                        if 0 <= ri < N and 0 <= rj < M:
                            if board[ri][rj] == 1:
                                queue.append((ri,rj))

    print(cnt)
