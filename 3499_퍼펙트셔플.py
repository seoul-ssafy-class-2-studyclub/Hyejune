test_num = int(input())

for t in range(test_num):

    N = int(input())
    base_list = list(input().split())
    result_list = []

    if N%2:
        x = 1
    else:
        x = 0

    l_01 = base_list[:int(N/2)+x]
    l_02 = base_list[int(N/2)+x:]

    for i in range(int(N/2)):
        result_list.append(l_01[i])
        result_list.append(l_02[i])
    
    if x == 1:
        result_list.append(l_01[-1])

    print('#' + str(t+1) + ' ', end = '')
    print(' '.join(result_list))