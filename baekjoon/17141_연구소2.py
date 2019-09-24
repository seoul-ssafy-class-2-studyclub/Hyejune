from pprint import pprint

D = [(1,0), (-1,0), (0,1), (0,-1)]


N, M = map(int,input().split())
virus_place = []
num_zero = 0
min_time = 9999
board = [0]*N
for i in range(N):
    board[i] = list(map(int,input().split()))
    for j in range(N):
        if board[i][j] == 2:
            virus_place.append((i,j))
        elif board[i][j] == 0:
            num_zero += 1

num_zero += len(virus_place) - M

def combi(k,arr,now):
    global min_time
    if k == len(virus_place) - M:
        temp_board = [0]*N
        temp_start = virus_place[:]
        for i in range(N):
            temp_board[i] = board[i][:]
        for temp_i, temp_j in arr:
            temp_board[temp_i][temp_j] = 0
            temp_start.remove((temp_i,temp_j))
        # print(temp_start)
        visited = [[False for j in range(N)] for i in range(N)]
        queue = temp_start
        cnt = 0
        time_count = 0
        flag = -1
        while queue:
            if cnt == num_zero:
                flag = 1
                break
            time_count += 1
            for a in range(len(queue)):
                temp_i, temp_j = queue.pop(0)
                visited[temp_i][temp_j] = True
                for b in range(4):
                    di, dj = D[b]
                    ri = temp_i + di
                    rj = temp_j + dj
                    if 0 <= ri < N and 0 <= rj < N and visited[ri][rj] == False and temp_board[ri][rj] == 0:
                        temp_board[ri][rj] = 2
                        queue.append((ri,rj))
                        cnt += 1
        if flag == 1:
            if time_count < min_time:
                min_time = time_count

        # pprint(temp_board)
        return
    else:
        for i in range(now+1, len(virus_place)):
            combi(k+1, arr + [virus_place[i]], i)

combi(0, [], -1)
if min_time == 9999:
    min_time = -1
print(min_time)
