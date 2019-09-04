from pprint import pprint
test_num = int(input())

for t in range(test_num):
    N, M = map(int,input().split())
    board = [0]*N
    for i in range(N):
        board[i] = list(map(int,input().split()))
    # print(board)

    max_num = 0 

    def sum_box(i,j):
        total = 0
        for a in range(M):
            for b in range(M):
                total += board[i+a][j+b]
        return total

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = sum_box(i,j)
            if total > max_num:
                max_num = total
    
    print('#' + str(t+1) + ' ',end='')
    print(max_num)
