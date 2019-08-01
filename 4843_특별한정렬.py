def my_max(a):                  # 최대값을 구하는 함수 my_max 정의
    max_int = a[0]
    for i in a:
        if i > max_int:
            max_int = i
    return max_int

def my_min(a):                  # 최소값을 구하는 함수 my_max 정의
    min_int = a[0]
    result = 0
    for i in a:
        if i < min_int:
            min_int = i
    return min_int

def my_sorting(a, x = -1):          # x=1이면 오름차순, x=-1이면 내림차순 정렬해주는 함수 정의
    sorted_list = []
    if x == 1:
        for i in range(len(a)):
            sorted_list.append(my_min(a))
            a.remove(my_min(a))
        return sorted_list
    if x == -1:
        for i in range(len(a)):
            sorted_list.append(my_max(a))
            a.remove(my_max(a))
        return sorted_list

    


# l = [3, 7, 4, 8, 2, 55, 22, 62, 30]
# print(my_sorting(l))

test_num = int(input())

for t in range(test_num):
    str_len = int(input())
    base_list = my_sorting(list(map(int, input().split())))

    sliced_list01 = base_list[:str_len//2]
    sliced_list02 = my_sorting(base_list[str_len//2:],1)

    result_list = []
    for i in range(str_len//2):
        result_list.append(sliced_list01[i])
        result_list.append(sliced_list02[i])
    
    if str_len % 2:
        result_list.append(sliced_list02[-1])

    # print(base_list)
    # print(sliced_list01)
    # print(sliced_list02)
    print('#' + str(t + 1) + ' ', end='')
    print(' '.join(map(str, result_list[:10])))
