from pprint import pprint
change = {0:(1,0), 1:(-1,0), 2:(0,1), 3:(0,-1)}
max_num = 0
N, M = map(int,input().split())
result_list = []
zero = []
virus = []
board = [0]*N

for i in range(N):                      # 보드 만들때 0 위치와 2의 위치(바이러스)를 미리 받아온다
    board[i] = list(map(int,input().split()))
    for j in range(M):
        if board[i][j] == 0:
            zero.append([i,j])
        elif board[i][j] == 2:
            virus.append([i, j])


def attack(t_b):
    for i in range(len(virus)):
        stack = [virus[i]]
        while stack:
            temp_a = stack[-1][0]
            temp_b = stack[-1][1]
            stack.pop()
            for i in range(4):
                da, db = change[i]
                if 0 <= temp_a+da < N and 0 <= temp_b+db < M and t_b[temp_a+da][temp_b+db] == 0:
                    t_b[temp_a + da][temp_b + db] = 2
                    stack.append([temp_a+da,temp_b+db])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if t_b[i][j] == 0:
                cnt += 1
    return cnt

# 0인 곳 중 3곳 골라서 벽세우기
def wall(k,arr,now):
    global max_num
    if k == 3:
        temp_board = [0] * N
        for i in range(N):
            temp_board[i] = board[i][:]
        for i in range(3):
            a, b = zero[arr[i]]
            temp_board[a][b] = 1
        temp_max = attack(temp_board)
        if temp_max > max_num:
            max_num = temp_max
        return
    else:
        for i in range(now+1, len(zero)):
            wall(k+1, arr+[i], i)

wall(0,[],-1)

print(max_num)