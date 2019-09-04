from pprint import pprint
test_num = int(input())
direction = {0:(1,0), 1:(1,1), 2:(0,1), 3:(-1,1), 4:(-1,0), 5:(-1,-1), 6:(0,-1), 7:(1,-1)}
color = {1:2, 2:1}

for t in range(test_num):
    N, M = map(int,input().split())
    queue = []
    board = [[0 for i in range(N)]for j in range(N)]
    board[N//2][N//2] = 2
    board[N//2 - 1][N//2 - 1] = 2
    board[N//2][N//2 - 1] = 1
    board[N//2 - 1][N//2] = 1
    for i in range(M):
        x, y, c = map(int,input().split())          # 가로, 세로, 컬러(1은 흑돌 2는 백돌)
        queue.append((x-1,y-1,c))
    
    def change(x, y, my_c, c, dx, dy):
        temp_store = [(x,y)]
    
        while True:
            current_x = temp_store[-1][0]
            current_y = temp_store[-1][1]
            if not (0 <= current_x + dx < N and 0 <= current_y + dy < N):
                return
            elif board[current_y + dy][current_x + dx] == 0:
                return
            elif board[current_y + dy][current_x + dx] == other_c:
                temp_store.append((current_x + dx, current_y + dy))
                continue
            else:
                for item in temp_store:
                    board[item[1]][item[0]] = my_c
                return

    while queue:
        temp_x, temp_y, temp_c =  queue.pop(0)
        other_c = color[temp_c]        
        board[temp_y][temp_x] = temp_c
        
        for i in range(8):
            dx = direction[i][0]
            dy = direction[i][1]
            if 0 <= temp_x + dx < N and 0 <= temp_y + dy < N:       # 범위상 2칸이상 갈곳이 있어야 가능성이 있는 케이스이므로
                if board[temp_y + dy][temp_x + dx] == 0 or board[temp_y + dy][temp_x + dx] == temp_c:
                    continue
                else:
                    change(temp_x + dx, temp_y + dy, temp_c, other_c, dx, dy)

    white = 0
    black = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                black += 1
            elif board[y][x] == 2:
                white += 1
    
    result = '%d %d' %(black, whilte)

    print('#' + str(t+1) + ' ', end = '')
    print(result)
    