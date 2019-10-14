from pprint import pprint
D = [(0,-1), (-1,0), (0,1), (1,0)]  # 서, 북, 동, 남
N, M = map(int, input().split())

info_board = [0] * M
for i in range(M):
    info_board[i] = list(map(int, input().split()))

# pprint(info_board)

real_board = [[0 for j in range(N)] for i in range(M)]

cnt = 0
for i in range(M):
    for j in range(N):
        if real_board[i][j] == 0:
            cnt += 1
            queue = [(i,j)]
            
            while queue:
                temp_i, temp_j = queue.pop(0)
                real_board[temp_i][temp_j] = cnt
                print(temp_i, temp_j)
                for i in range(4):
                    if not info_board[temp_i][temp_j] & (1 << i):
                        di, dj = D[i]
                        ri = temp_i + di
                        rj = temp_j + dj
                        if 0 <= ri < M and 0 <= rj < N:
                            if real_board[ri][rj] == 0:
                                real_board[ri][rj] = cnt
                                queue.append((ri,rj))
                                print('왜왜왜')


pprint(real_board)