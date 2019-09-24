from pprint import pprint

D = [(0,1), (1,0)]

test_num = int(input())

for t in range(test_num):
    result = 0
    N = int(input())
    board = [0] * N
    for i in range(N):
        board[i] = list(map(int,input().split()))

    mi = 9999

    def func(k, i, j, su):
        global mi
        if k == 2 * N - 1:
            if mi > su:
                mi = su
            return
        else:
            for a in range(2):
                di, dj = D[a]
                ri = i + di
                rj = j + dj
                if 0 <= ri < N and 0 <= rj < N:
                    func(k+1, ri, rj, su + board[ri][rj])
    
    func(0, 0, 0, board[0][0])

    print('#' + str(t+1) + ' ', end='')
    print(mi)