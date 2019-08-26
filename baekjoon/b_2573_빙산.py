from pprint import pprint
N, M = map(int,input().split())

board = [0] * N
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    board[i] = list(map(int, input().split()))

def FirstIdx(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                return [i,j]
    return False

def iceberg(arr):
    temp_arr = [0]*N            # 판별에 사용할 임시보드 복사(deep copy)
    for i in range(N):
        temp_arr[i] = arr[i][:]
    if FirstIdx(arr) == 1:
        return 1
    else:   
        stack = [FirstIdx(arr)]
    visted = [0]*N
    for i in range(N):  
        visted[i] = [False]*M

    while stack:
        temp_x = stack[-1][0]
        temp_y = stack[-1][1]
        stack.pop(-1)
        if visted[temp_x][temp_y] == False:
            visted[temp_x][temp_y] = True
            temp_arr[temp_x][temp_y] = 0
            for i in range(4):
                if 0 <= temp_x+dx[i] < N and 0 <= temp_y+dy[i] < M and temp_arr[temp_x+dx[i]][temp_y+dy[i]] > 0:
                    stack.append([temp_x+dx[i],temp_y+dy[i]])
        # pprint(temp_arr)
    

    if FirstIdx(temp_arr) == False:     # 빙산이 하나면
        return True                     # True리턴
    else:                               # 빙산이 나눠졌으면
        return False                    # False리턴


    

def melt(idx):
    stack = [idx]
    visted = [0]*N
    idx_list = []
    for i in range(N):
        visted[i] = [False]*M

    while stack:
        temp_x = stack[-1][0]
        temp_y = stack[-1][1]
        # print(stack)
        stack.pop(-1)
        if visted[temp_x][temp_y] == False:
            visted[temp_x][temp_y] = True
            for i in range(4):
                if 0 <= temp_x+dx[i] < N and 0 <= temp_y+dy[i] < M and board[temp_x+dx[i]][temp_y+dy[i]] == 0 and board[temp_x][temp_y] > 0:
                    if board[temp_x][temp_y] == 1:
                        idx_list.append([temp_x, temp_y])
                    else:
                        board[temp_x][temp_y] -= 1
                        
                elif 0 <= temp_x+dx[i] < N and 0 <= temp_y+dy[i] < M:
                    stack.append([temp_x+dx[i],temp_y+dy[i]])
                    
    for item in idx_list:
        board[item[0]][item[1]] = 0    
            
# melt([1,1])
cnt = 0

while iceberg(board):
    if iceberg(board) == 1:
        cnt = 0
        break
    melt(FirstIdx(board))
    pprint(board)
    # for i in range(N):
    #     for j in range(M):
    #         if board[i][j] == -1:
    #             board[i][j] = 0
    cnt += 1


print(cnt)

