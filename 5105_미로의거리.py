from pprint import pprint
test_num = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for t in range(test_num):
    N = int(input())
    maze = [0] * N
    visited = [0] * N
    for i in range(N):
        maze[i] = list(map(int,list(input())))
        # visited[i] = [False] * N

    def FindFirst():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    return [i,j]

    queue = [FindFirst()]
    # visited[queue[0][0]][queue[0][1]] = True
    cnt = 0
    flag = 0
    while queue:
        cnt -= 1
        for i in range(len(queue)):
            temp_x = queue[0][0]
            temp_y = queue[0][1]
            queue.pop(0)
            for j in range(4):
                if 0 <= temp_x+dx[j] < N and 0 <= temp_y+dy[j] < N:
                    if maze[temp_x+dx[j]][temp_y+dy[j]] == 0:
                        maze[temp_x+dx[j]][temp_y+dy[j]] = cnt
                        queue.append([temp_x+dx[j],temp_y+dy[j]])
                    elif maze[temp_x+dx[j]][temp_y+dy[j]] == 3:
                        flag = 1
                        break
            if flag == 1:
                break
        
        if flag ==1:
            break
        pprint(maze)
    
    if flag == 0:
        cnt = -1
    result = -cnt-1
    print('#' + str(t+1) + ' ', end='')
    print(result)