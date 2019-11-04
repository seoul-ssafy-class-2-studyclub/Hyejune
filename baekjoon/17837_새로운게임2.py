from pprint import pprint

direction = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
change_d = {1:2, 2:1, 3:4, 4:3}

N, K = map(int, input().split())

original_board = [0]*N
for i in range(N):
    original_board[i] = list(map(int, input().split()))

chess_idx = [0]*(K+1)
real_board = [[[] for j in range(N)] for i in range(N)]
for i in range(1,K+1):
    a, b, d = list(map(int, input().split()))
    real_board[a-1][b-1].append(i)
    chess_idx[i] = [a-1,b-1,d]


pprint(real_board)
print(chess_idx)

cnt = 0

def move(arr):
    temp_i, temp_j, temp_d = arr[0]
    di, dj = direction[temp_d]
    ri = temp_i + di
    rj = temp_j + dj
    if (not (0 <= ri < N and 0 <= rj < N)) or original_board[ri][rj] == 2:
        if original_board[ri][rj] == 0:
            original_board[temp_i][temp_j] 



while True:
    if cnt == 1:
        break
    cnt += 1
    if cnt > 1000:
        break
    for i in range(1, K+1):
        ti, tj, td = chess_idx[i]
        temp_len = len(original_board[ti][tj])
        if temp_len == 1:
            move([chess_idx[i]])
        elif temp_len > 1:
            for l in range(temp_len):
                if original_board[ti][tj][l] == i:
                    temp_num = l
                if l == temp_len - 1:
                    move([chess_idx[i]])
                else:
                    move([chess_idx[temp_num:]])



if cnt > 1000:
    cnt = -1

print(cnt)
