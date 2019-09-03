from pprint import pprint
test_num = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for t in range(test_num):

    N = int(input())
    num = 0
    board = [0]*N
    result_list = []
    for i in range(N):
        board[i] = list(map(int,input().split()))

    def findFirst():
        for i in range(N):
            for j in range(N):
                if board[i][j] > 0:
                    return [i,j]
        return False

    def findLength(i,j):
        global num
        num += 1
        cnt_i = 1
        cnt_j = 1
        while True:                 # 가로길이 재는 부분
            if i == N-1 or board[i+1][j] == 0:
                break
            cnt_i += 1
            i += 1
            
        while True:                 # 세로길이 재는 부분
            if j == N-1 or board[i][j+1] == 0:
                break
            cnt_j += 1
            j += 1
        return cnt_i,cnt_j
        
    def changeBoard(i,j):
        global num
        board[i][j] = -num
        for a in range(4):
            if 0 <= i + dx[a] < N and 0 <= j + dy[a] < N:
                if board[i + dx[a]][j + dy[a]] > 0:
                    board[i + dx[a]][j + dy[a]] = -num
                    changeBoard(i + dx[a],j + dy[a])

    while findFirst():
        i, j = findFirst()
        a,b = findLength(i,j)
        mul = a * b
        result_list.append([mul,a,b])
        changeBoard(i,j)
        
    result_list.sort()

    print('#' + str(t+1) + ' ', end='')
    print(num,end=' ')
    for a in range(len(result_list)):
        print(result_list[a][1],result_list[a][2], end =' ')
    print()

