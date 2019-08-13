def LadderUp(i, j):
    if i == 0:
        return j
    else:
        if j != 0 and j != 99:
            if base_list[i][j-1] == 1:
                base_list[i][j] = -1
                j -= 1

            elif base_list[i][j+1] == 1:
                base_list[i][j] = -1
                j += 1

            elif base_list[i-1][j] == 1:
                base_list[i][j] = -1
                i -= 1
            return LadderUp(i, j)
        elif j == 0:
            if base_list[i][j+1] == 1:
                base_list[i][j] = -1
                j += 1

            elif base_list[i-1][j] == 1:
                base_list[i][j] = -1
                i -= 1
            return LadderUp(i, j)
        elif j == 99:
            if base_list[i][j-1] == 1:
                base_list[i][j] = -1
                j -= 1
            elif base_list[i-1][j] == 1:
                base_list[i][j] = -1
                i -= 1
            return LadderUp(i, j)



for t in range(10):
    result = 0
    N = int(input())
    base_list = []
    for i in range(100):
        base_list.append(list(map(int,input().split())))

    a = 99                          # 초기 i 인덱스 = 99
    b = base_list[-1].index(2)

    # print(b)

    # print('결과는')
    # print(LadderUp(a, b))

    print('#' + str(t+1) + ' ', end='')
    print(LadderUp(a, b))
        
# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 1