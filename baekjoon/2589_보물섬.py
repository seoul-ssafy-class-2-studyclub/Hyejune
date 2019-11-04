# BFS, queue에 들어있는것들 묶어서 처리

D = [(1,0), (0,1), (-1,0), (0,-1)]
max_result = 0


N, M = map(int, input().split())

board = [0]*N
for i in range(N):
    board[i] = list(input())



for i in range(N):
    for j in range(M):
        cnt = -1
        if board[i][j] == 'L':
            visited = [[False for b in range(M)] for a in range(N)]
            visited[i][j] = True
            queue = [(i,j)]
            while queue:
                cnt += 1
                for _ in range(len(queue)):
                    temp_i, temp_j = queue.pop(0)
                    for l in range(4):
                        di, dj = D[l]
                        ri = temp_i + di
                        rj = temp_j + dj
                        if 0 <= ri < N and 0 <= rj < M:
                            if not visited[ri][rj]:
                                if board[ri][rj] == 'L':
                                    visited[ri][rj] = True
                                    queue.append((ri,rj))
        if cnt > max_result:
            max_result = cnt
                    


print(max_result)
