# 다익스트라 알고리즘

from pprint import pprint
from heapq import heappop, heappush
D = [(0,1), (1,0), (0,-1), (-1,0)]
cnt = 0

while True:
    cnt += 1
    N = int(input())

    if N == 0:
        break

    board = [0]*N
    for i in range(N):
        board[i] = list(map(int, input().split()))

    queue = []

    money_loss = [[999999 for j in range(N)] for i in range(N)]

    money_loss[0][0] = board[0][0]

    heappush(queue, (board[0][0],0,0))

    while queue:
        temp_loss, temp_i, temp_j = heappop(queue)

        if temp_loss > money_loss[temp_i][temp_j]:
            continue

        for k in range(4):
            di, dj = D[k]
            ri = temp_i + di
            rj = temp_j + dj
            if 0 <= ri < N and 0 <= rj < N:
                temp = temp_loss + board[ri][rj]
                if money_loss[ri][rj] > temp:
                    money_loss[ri][rj] = temp
                    heappush(queue, (temp, ri, rj))

    print("Problem " + str(cnt) + ": ", end='')
    print(money_loss[N-1][N-1])