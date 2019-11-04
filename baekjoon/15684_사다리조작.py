
from pprint import pprint

N, M, H = map(int, input().split())     # N은 세로수 갯수(뼈대), M은 가로수 개수(현재), H는 가로선을 놓을수있는 개수

ladder_board = [[0 for j in range(N)] for i in range(H)]
flag = -1

# pprint(ladder_board)

def downdown(board):
    # global flag
    for j in range(N):
        temp_i = 0
        temp_j = j
        while True:
            if temp_i == H:
                if temp_j != j:
                    return False
                break
            if board[temp_i][temp_j] == 0:
                temp_i += 1
            elif board[temp_i][temp_j] == 1:
                temp_i += 1
                temp_j += 1
            elif board[temp_i][temp_j] == 2:
                temp_i += 1
                temp_j -= 1
    return True

def comb(pick_num, k, arr, now, t_b):
    global flag
    if flag != -1:
        return
    if k == pick_num:
        if downdown(t_b) == True:
            flag = pick_num
        return 
    else:
        for i in range(now + 1, len(candidate)):
            temp_board = [0 for a in range(H)]
            for a in range(H):
                temp_board[a] = t_b[a][:]
            temp_i, temp_j = candidate[i]
            if temp_board[temp_i][temp_j] == 0 and temp_board[temp_i][temp_j+1] != 1:
                temp_board[temp_i][temp_j] = 1
                temp_board[temp_i][temp_j+1] = 2
            comb(pick_num, k+1, arr + [candidate[i]], i, temp_board)


for i in range(M):
    temp_i, temp_j = map(int, input().split())
    ladder_board[temp_i-1][temp_j-1] = 1                # 인덱스 1씩 차이나니까
    ladder_board[temp_i-1][temp_j] = 2



candidate = []

for i in range(H):
    for j in range(N-1):
        if ladder_board[i][j] == 0 and ladder_board[i][j+1] != 1:
            candidate.append((i,j))

# print(candidate)

if downdown(ladder_board) == True:
    flag = 0
else:
    for i in range(1,4):
        # print(str(i) + '번째')
        comb(i, 0, [], -1, ladder_board)

        if flag != -1:
            break
    
# 가로 사다리 2개 놓기 ==> True반환시 거기서 끝
    # candidate에서 두개 고르고 downdown 돌리기 ==> 고를때 2개가 서로 간섭되는 관계면 중간에 컷

# 가로 사다리 3개 놓기 ==> True반환시 거기서 끝, 여기서도 안되면 -1출력
    # candidate에서 세개 고르고 downdown 돌리기 ==> 고를때 3개가 서로 간섭되는 관계면 중간에 컷


print(flag)