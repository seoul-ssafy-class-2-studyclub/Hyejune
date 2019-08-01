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

test_num = int(input())

for t in range(test_num):
    base_list = list(map(int, input().split()))
    
    result_list = []

    for a in base_list:
        for b in base_list[base_list.index(a)+1:]:
            for c in base_list[base_list.index(b)+1:]:
                result_list.append(a + b + c)
                # 인덱스로 바꿔주기

    
    result_list = list(set(result_list))
    

    print('#' + str(t + 1) + ' ', end='')
    print(my_sorting(result_list)[4])