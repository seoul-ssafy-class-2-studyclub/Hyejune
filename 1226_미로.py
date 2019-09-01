from pprint import pprint
n = 16  # 16 * 16 행렬
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for t in range(10):
    board = [0]*n
    num = int(input())  # 문제에서 주는 index 인풋값 - 의미없음
    result =0
    
    for i in range(n):
        board[i] = list(map(int,list(input())))

    # 도착지점의 좌표 찾아두기
    def FindFirst():
        for i in range(n):
            for j in range(n):
                if board[i][j] ==2:
                    return [i,j]

    stack = [FindFirst()]
    # visited = [0]*n
    # for i in range(n):
    #     visited[i] = [False]*n

    while stack:
        if result == 1:
            break
        temp_x = stack[-1][0]
        temp_y = stack[-1][1]
        stack.pop()

        
        for i in range(4):
            if 0 <= temp_x + dx[i] < n and 0 <= temp_y + dy[i] < n:
                if board[temp_x + dx[i]][temp_y + dy[i]] == 0:
                    board[temp_x + dx[i]][temp_y + dy[i]] = -1
                    stack.append([temp_x + dx[i], temp_y + dy[i]])
                elif board[temp_x + dx[i]][temp_y + dy[i]] == 3:
                    result = 1
                    break
                
    # pprint(board)
    print('#' + str(t+1) + ' ',end='')
    print(result)










