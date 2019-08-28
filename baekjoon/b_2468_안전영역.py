from pprint import pprint

N = int(input())

board = [0]*N
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    board[i] = list(map(int, input().split()))


def StartIdx(arr, h):         # 물
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h:
                return [i,j]
    return False

def SafeLand(height):      # 물 깊이를 인자로 받아 안전영역의 갯수를 반환하는 함수
    temp_arr = [0]*N
    visited = [0]*N
    cnt = 0

    for i in range(N):
        temp_arr[i] = board[i][:]
        visited[i] = [False] * N

    # pprint(temp_arr)

    while StartIdx(temp_arr, height) != False:
        cnt += 1
        stack = [StartIdx(temp_arr, height)]
        while stack:
            temp_x = stack[-1][0]
            temp_y = stack[-1][1]
            stack.pop()
            if visited[temp_x][temp_y] == False:
                temp_arr[temp_x][temp_y] = -(cnt)
                visited[temp_x][temp_y] = True
                for i in range(4):
                    if 0 <= temp_x+dx[i] < N and 0 <= temp_y+dy[i] < N and temp_arr[temp_x+dx[i]][temp_y+dy[i]] > height:
                        stack.append([temp_x+dx[i], temp_y+dy[i]])
        # pprint(temp_arr)
    return cnt

max_result = 0
for i in range(101):
    temp = SafeLand(i)
    if temp > max_result:
        max_result = temp
    if temp == 0:
        break


print(max_result)
# print(StartIdx(board, 7))
# SafeLand(4)
