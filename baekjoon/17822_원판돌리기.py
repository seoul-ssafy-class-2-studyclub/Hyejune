from pprint import pprint

D = [(0,1), (1,0), (0,-1), (-1,0)]

N,M,T = map(int,input().split())
print(N, M, T)
board = [0] * N

num_num = N * M      # 원판위 숫자의 개수
total_sum = 0       # 원판위 숫자들의 합

for i in range(N):
    board[i] = list(map(int, input().split()))
    total_sum += sum(board[i])

# total_sum 을 처음에 계산했다가 숫자 지울때마다 여기서 빼준다
# 지워지는 수가 아무것도 없는 경우 avg보다 큰수는 -1, 작은수는 +1 해준다
# 이때 avg = total // num_num 하고 하나씩 돌면서 비교하고 해당수도 바꾸어주고 total_sum 도 바꿔준다.
command = []
for i in range(T):
    command.append(list(map(int, input().split())))

# print(total_sum)

def rotate(n,dd):
    if dd == 0:
        temp = board[n].pop()
        board[n].insert(0,temp)
    else:
        temp = board[n].pop(0)
        board[n].append(temp)

for i in range(T):
    flag = 0
    x, d, k = command[i]
    # print(x,d,k)
    for j in range(N):
        if (j+1) % x == 0:
            for _ in range(k):
                rotate(j,d)
    # print(board)
    for a in range(N):
        for b in range(M):
            if board[a][b] != -100:
                visited = [[False for _ in range(M)] for __ in range(N)]
                temp_list = [(a,b)]
                queue = [(a,b)]
                visited[a][b] = True
                while queue:
                    temp_i, temp_j = queue.pop(0)
                    for p in range(4):
                        di, dj = D[p]
                        ri = temp_i + di
                        rj = temp_j + dj
                        if 0 <= ri < N:
                            if rj == -1:
                                rj = M-1
                            if rj == M:
                                rj = 0
                            if visited[ri][rj] == False and board[ri][rj] == board[a][b]:
                                visited[ri][rj] = True
                                queue.append((ri,rj))
                                temp_list.append((ri,rj))
            else: temp_list = []

            if len(temp_list) > 1:
                flag = 1
                # if i == 2:
                #     print(temp_list)
                for item in temp_list:
                    t_i, t_j = item
                    # if i == 2:
                    #     print(temp_list)
                    total_sum -= board[t_i][t_j]
                    num_num -= 1
                    board[t_i][t_j] = -100
    if num_num == 0:
        break
    if flag == 0:
        avg_now = total_sum / num_num
        for aa in range(N):
            for bb in range(M):
                if board[aa][bb] > avg_now:
                    board[aa][bb] -= 1
                    total_sum -= 1
                elif board[aa][bb] != -100 and  board[aa][bb] < avg_now :
                    board[aa][bb] += 1
                    total_sum += 1



    
print(total_sum)
