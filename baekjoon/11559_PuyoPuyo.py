from pprint import pprint
D = [(1,0), (0,1), (-1,0), (0,-1)]
combo_cnt = 0
flag = True
board = [0 for i in range(12)]
for i in range(12):
    board[i] = list(input())
​
def findPuyoGroup():
    global flag
    global combo_cnt
    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                temp_cnt = 1
                temp_char = board[i][j]
                temp_arr = [(i,j)]
                queue = [(i,j)]
                visited = [[False for a in range(6)] for b in range(12)]
                while queue:
                    for _ in range(len(queue)):
                        temp_i, temp_j = queue.pop(0)
                        visited[temp_i][temp_j] = True
                        for n in range(4):
                            di, dj = D[n]
                            ri = temp_i + di
                            rj = temp_j + dj
                            if 0 <= ri < 12 and 0 <= rj < 6:
                                if visited[ri][rj] == False:
                                    if board[ri][rj] == temp_char:
                                        temp_cnt += 1
                                        temp_arr.append((ri,rj))
                                        queue.append((ri,rj))
                if temp_cnt >= 4:
                    flag = True
                    for item in temp_arr:
                        t1, t2 = item
                        board[t1][t2] = '.'
    if flag == True:
        combo_cnt += 1
​
def down(i, j):
    if i == 11:
        return
    if board[i+1][j] == '.':
        board[i+1][j] = board[i][j]
        board[i][j] = '.'
        down(i+1, j)
    
​
def fallingPuyo():
    for i in range(10, -1, -1):
        for j in range(6):
            if board[i][j] != '.':
                down(i,j)
​
​
​
while flag:
    if not flag:
        break
    findPuyoGroup()
    # pprint(board)
    fallingPuyo()
    # pprint(board)
​
print(combo_cnt)