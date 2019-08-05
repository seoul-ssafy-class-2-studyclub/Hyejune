test_num = int(input())

for t in range(test_num):

    base_list = list(map(int,input()))
    
    # print(base_list)

    cnt = 0

    clapping_n = base_list[0]
    # print(cnt)
    for i in range(1,len(base_list)):
        if clapping_n < i and base_list[i] != 0:
            cnt += i - clapping_n
            clapping_n = i + base_list[i]
        else:
            clapping_n += base_list[i]
        # print(cnt)

    result = 0
    print('#' + str(t+1) + ' ', end = '')
    print(cnt)