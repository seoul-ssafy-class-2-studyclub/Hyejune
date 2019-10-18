# 디피 추가하기

isitEmpty = [[[(0,2)], [(0,2), (1,2), (1,1)]], [[(2,0)], [(1,1), (2,1), (2,0)]], [[(1,2)], [(2,1)], [(1,2), (2,2), (2,1)]]]

change = [[0, 2], [1, 2], [0, 1, 2]]

move = {0:(0,1), 1:(1,0), 2: (1,1)}

N = int(input())

DP = {}
cnt = 0
board = [0] * N 
for i in range(N):
    board[i] = list(map(int, input().split()))

def movePipe(temp_i, temp_j, s):
    global cnt
    if temp_i == N - 2 and temp_j == N - 2 and s == 2:
        cnt += 1
        return
    elif temp_i == N - 2 and temp_j == N - 1 and s == 1:
        cnt += 1 
        return
    elif temp_j == N - 2 and temp_i == N - 1 and s == 0:
        cnt += 1
        return
    for a in range(len(change[s])):
        flag = 1
        for b in range(len(isitEmpty[s][a])):
            di, dj = isitEmpty[s][a][b]
            ri = temp_i + di
            rj = temp_j + dj
            if 0 <= ri < N and 0 <= rj < N:
                if board[ri][rj] != 0:
                    flag = -1
            else:
                flag = -1
        if flag == 1:
            ii, jj = move[s]
            movePipe(temp_i + ii, temp_j + jj, change[s][a])



movePipe(0, 0, 0)

print(cnt)