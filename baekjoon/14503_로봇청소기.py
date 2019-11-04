Dchange = {0:3, 1:0, 2:1, 3:2}
D_left = {0:(0,-1), 1:(-1,0), 2:(0,1), 3:(1,0)}
D_back = {0:(1,0), 1:(0,-1), 2:(-1,0), 3:(0,1)}

N, M = map(int, input().split())

r, c, d = map(int, input().split()) 

board = [0]*N
for i in range(N):
    board[i] = list(map(int, input().split()))

def clean(temp_i,temp_j):
    board[temp_i][temp_j] = -1

def search_move(current_i, current_j, current_d,k):
    global r
    global c
    global d
    if k == 4:
        t_i, t_j = D_back[current_d]
        ri = current_i + t_i
        rj = current_j + t_j
        if board[ri][rj] == 1:
            # print('음?')
            r = -1
            return
            # return [-1,-1,-1]          # 실행할게 없는경우
        else:
            # print('엥;')
            r = ri
            c = rj
            d = current_d
            return
            # return [ri,rj,current_d]
    t_i, t_j = D_left[current_d]
    ri = current_i + t_i
    rj = current_j + t_j

    if board[ri][rj] == 0:
        # print('모지')
        r = ri
        c= rj
        d = Dchange[current_d]
        return
        # return [ri,rj,Dchange[current_d]]
    else:
        # print('왜지')
        search_move(current_i, current_j, Dchange[current_d],k+1)
        return

flag = 0
cnt = 0
while True:
    if r == -1:
        break

    if board[r][c] == 0:
        clean(r,c)
        cnt += 1
    
    move = 0
    search_move(r,c,d,0)

    

print(cnt)
