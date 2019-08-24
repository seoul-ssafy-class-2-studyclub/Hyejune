position_list = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (1, -1), (-1, 1)]
def convertZero(square_list, i, j):
    for (x, y) in position_list:
        if square_list[i+x][j+y] == '*':
            square_list[i][j] = 'n'
        if square_list[i][j] == 'n':
            break




test_num = int(input())

for t in range(test_num):
    n = int(input())
    base_list = []

    for i in range(n):
        base_list.append(list(input()))

    for i in range(1,n-1):
        for j in range(1,n-1):
            if base_list[i][j] == '.':
                convertZero(base_list, i, j)


    print('#' + str(t + 1) + ' ')
    for i in range(n):
        print(base_list[i])