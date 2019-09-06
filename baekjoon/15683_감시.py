D = {
    1:[[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
    2:[[(1,0), (-1,0)], [(0,1), (0,-1)]],
    3:[[(1,0),(0,1)], [(0,1),(-1,0)], [(-1,0),(0,-1)], [(0,-1),(1,0)]],
    4:[[(0,1), (0,-1), (1,0)], [(0,1), (0,-1), (-1,0)], [(0,1), (1,0), (-1,0)], [(0,-1), (1,0), (-1,0)]],
    5:[[(0,1), (0,-1), (1,0), (-1,0)]]
    }

camera_list = []
num_zero = 0
camera_count = 0

N, M = map(int,input().split())
board = [0]*N
for i in range(N):
    board[i] = list(map(int,input().split()))
    for j in range(N):
        if board[i][j] != 0 and board[i][j] != 6:
            camera_list.append((i,j))
            camera_count += 1
        elif board[i][j] == 0:
            num_zero += 1

print(camera_list)

def combi(k, arr):
    if k == len(camera_list):
        print(arr)
        # temp_board = [0] * N
        # for i in range(N):
        #     temp_board[i] = board[i][:]
        
        # visited = [[False for j in range(N)] for i in ran(N)]
        # queue = camera_list[:]
        # while queue:
        #     temp_i, temp_j = queue.pop(0)
        #     for di, dj in arr[idx]:
        #         ri = temp_i + di
        #         rj = temp_j + dj
        #         if 0 <= ri < N and 0 <= rj < N and visited[ri][rj] == False:
        #             temp_board[ri][rj] = -1
        #             visited[ri][rj] = True
        #     idx += 1

        return
    else:
        temp_i, temp_j = camera_list[k]
        temp_cam_num = board[temp_i][temp_j]
        for item in D[temp_cam_num]:
            combi(k+1, arr + [item])

combi(0, [])