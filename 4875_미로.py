from pprint import pprint

test_num = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for t in range(test_num):
    N = int(input())

    board = [0]*N
    for i in range(N):
        board[i] = list(input())

    for i in range(N):
        for j in range(N):
            if board[i][j] == '2':
                st_i = i
                st_j = j
                break

    visited = [0]*N
    for i in range(N):
        visited[i] = [False]*N
    
    result = 0
    stack = [[st_i, st_j]]
    
    while stack:
        temp_x = stack[-1][0]
        
        temp_y = stack[-1][1]
        stack.pop()
        if visited[temp_x][temp_y] == False:
            visited[temp_x][temp_y] = True
            board[temp_x][temp_y] = '9'
            for i in range(4):
                if 0 <= temp_x+dx[i] < N and 0 <= temp_y+dy[i] < N:
                    if board[temp_x+dx[i]][temp_y+dy[i]] == '0':
                        stack.append([temp_x+dx[i], temp_y+dy[i]])
                    elif board[temp_x+dx[i]][temp_y+dy[i]] == '3':
                        result = 1
                        break
    
    print('#' + str(t+1) + ' ', end='')
    print(result)

