def my_max(a):
    ma = a[0]
    for i in range(len(a)):
        if a[i] > ma:
            ma = a[i]
    return ma

# def my_sum(a):
#     s = 0
#     for i in range(len(a)):
#         s += a[i]
#     return s


for t in range(10):
    N = int(input())
    base_list = []
    result_list = []
    
    for i in range(100):
        base_list.append(list(map(int, input().split())))

    # print(base_list)
    for i in range(100):
        su = 0
        for j in range(100):
            su += base_list[i][j]
        result_list.append(su)


    for i in range(100):
        su = 0
        for j in range(100):
            su += base_list[j][i]
        result_list.append(su)
    
    cross_s01 = 0
    cross_s02 = 0
    for i in range(100):
        cross_s01 += base_list[i][i]
        cross_s02 += base_list[-1-i][-1-i]
    
    result_list.append(cross_s01)
    result_list.append(cross_s02)

    
    print('#' + str(N) + ' ', end = '')
    print(my_max(result_list))