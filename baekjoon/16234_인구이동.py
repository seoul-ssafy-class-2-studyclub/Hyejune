from pprint import pprint
D = [(1,0), (-1,0), (0,1), (0,-1)]
N, L, R = map(int, input().split())
total_count = 0

visited = [[False for j in range(N)] for i in range(N)]
board = [0]*N
for i in range(N):
    board[i] = list(map(int,input().split()))

def FindFalse():
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                return (i,j)
    return False

total_count = 0
def my_func():
    cnt = 0
    while True:
        if FindFalse() == False:
            break
        a,b = FindFalse()
        # print(a,b)
        stack = [(a,b)]
        visited[a][b] = True
        temp_list = [(a,b)]
        temp_sum = board[a][b]
        while stack:
            i, j = stack.pop()
            visited[i][j] = True
            for c in range(4):
                di, dj = D[c]
                ri = i + di
                rj = j + dj
                if 0 <= ri < N and 0 <= rj < N and L <= abs(board[i][j]-board[ri][rj]) <= R and visited[ri][rj] == False:
                    visited[ri][rj] = True
                    stack.append((ri,rj))
                    temp_list.append((ri,rj))
                    temp_sum += board[ri][rj]
        if len(temp_list) > 1:
            cnt += 1
        temp_average = temp_sum // len(temp_list)
        for di2, dj2 in temp_list:
            board[di2][dj2] = temp_average
    return cnt

while True:
    visited = [[False for j in range(N)] for i in range(N)]
    temp = my_func()
    if temp == 0:
        break
    total_count += 1
    
print(total_count)









