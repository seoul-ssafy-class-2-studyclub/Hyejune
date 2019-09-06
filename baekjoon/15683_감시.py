from pprint import pprint
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
min_val = 9999

N, M = map(int,input().split())
board = [0]*N
for i in range(N):
    board[i] = list(map(int,input().split()))
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            camera_list.append((i,j))
            camera_count += 1
        if board[i][j] == 0:
            num_zero += 1


def combi(k, arr):
    global min_val
    if k == len(camera_list):
    
        temp_board = [0] * N
        for i in range(N):
            temp_board[i] = board[i][:]
        temp_zero = num_zero
        for i in range(camera_count):
            temp_i, temp_j = camera_list[i]
            for item in arr[i]:
                di, dj = item
                ri = temp_i + di
                rj = temp_j + dj
                while True:
                    if 0 <= ri < N and 0 <= rj < M:
                        if board[ri][rj] == 6:
                            break
                        if temp_board[ri][rj] == 0:
                            temp_board[ri][rj] = -1
                            temp_zero -= 1
                        ri += di
                        rj += dj
                    else:
                        break
        if temp_zero < min_val:
            min_val = temp_zero
        return
    else:
        temp_i, temp_j = camera_list[k]
        temp_cam_num = board[temp_i][temp_j]
        for item in D[temp_cam_num]:
            combi(k+1, arr + [item])

combi(0, [])

print(min_val)