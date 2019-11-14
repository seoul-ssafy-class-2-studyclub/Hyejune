from pprint import pprint

D = [(0,1), (1,0), (0,-1), (-1,0)]

test_num = int(input())

for t in range(test_num):

    N, W, H = map(int, input().split())

    num_brick = 0

    board = [0] * H
    for i in range(H):
        board[i] = list(map(int, input().split()))
        for j in range(W):
            if board[i][j] != 0:
                num_brick += 1


    # pprint(board)

    min_result = 999999
    
    def downdown(b):
        for j in range(W):
            temp = []
            for i in range(H):
                if b[i][j] != 0:
                    temp += [b[i][j]]
            for i in range(1,len(temp)+1):
                b[-i][j] = temp[-i]
            for i in range(H - len(temp)):
                b[i][j] = 0
        
        return b



    def destroy(boardboard, j, new_brick):
        current_num = 0
        for i in range(H):
            if boardboard[i][j] != 0:
                current_num = boardboard[i][j]
                break
        if current_num == 0:
            # print('음..?')
            return [boardboard, new_brick]
        queue = [(i,j,current_num)]
        while queue:
            temp_i, temp_j, temp_num = queue.pop(0)
            if boardboard[temp_i][temp_j] != 0:
                boardboard[temp_i][temp_j] = 0
                new_brick -= 1
            for l in range(4):
                di, dj = D[l]
                for m in range(1,temp_num):
                    ri = temp_i + di * m
                    rj = temp_j + dj * m
                    if 0 <= ri < H and 0 <= rj < W:
                        temptemp = boardboard[ri][rj]
                        if temptemp != 0:
                            boardboard[ri][rj] = 0
                            new_brick -= 1
                            if temptemp != 1:
                                queue.append((ri,rj,temptemp))
        
        return [downdown(boardboard), new_brick]

    def pick(k, temp_board, remaining_brick):
        global min_result
        if k == N:
            # print('dddddd')
            # print(remaining_brick)
            if min_result > remaining_brick:
                min_result = remaining_brick
            return
        else:
            for j in range(W):
                new_temp = [0] * H
                for l in range(H):
                    new_temp[l] = temp_board[l][:]
                temp_state = destroy(new_temp,j, remaining_brick)
                pick(k+1, temp_state[0], temp_state[1])



    pick (0, board, num_brick)
    print('#' + str(t+1) + ' ', end='')
    print(min_result)