test_num = int(input())

def turn(l, length):
    new_list = []
    for i in range(length):
        new_list.append([])
    for i in range(length):
        for j in range(length):
            new_list[i].append(0)
    
    # print(new_list)
    for i in range(length):
        for j in range(length):
            new_list[i][j] = l[j][i]
        new_list[i].reverse()
    return new_list

for num in range(test_num):
    N = int(input())

    base_list = []
    for i in range(N):
        base_list.append(list(map(int, input().split())))
    # print(base_list)
    result_list01 = turn(base_list, N)
    result_list02 = turn(result_list01, N)
    result_list03 = turn(result_list02, N)

    print('#' + str(num + 1))
    for i in range(N):
        print(''.join(map(str, result_list01[i])), end = ' ')
        print(''.join(map(str, result_list02[i])), end = ' ')
        print(''.join(map(str, result_list03[i])), end = ' ')
        print()


# n_list = [[0]*10 for i in range(10)]
# print(n_list)