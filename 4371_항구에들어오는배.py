test_num = int(input())

for t in range(test_num):
    N = int(input())
    base_list = []
    result_list = []
    sub_list = []
    for i in range(N):
        base_list.append(int(input()))

    for i in range(1, N):
        if i == 1:
            result_list.append(base_list[1]-1)
        else:
            result_list.append(base_list[i]-base_list[0])

    for i in range(len(result_list)-1):
        for j in range(i +1, len(result_list)):
            if result_list[j] % result_list[i] == 0:
                sub_list.append(result_list[j])
    
    for item in sub_list:
        if item in result_list:
            result_list.remove(item)
                
    

    print('#' + str(t + 1) + ' ', end = '')
    print(len(result_list))

