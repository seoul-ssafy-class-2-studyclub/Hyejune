def my_max(a):                  # 최대값을 구하는 함수 my_max 정의
    max_int = a[0]
    for i in a:
        if i > max_int:
            max_int = i
    return max_int
 
def my_LIS(a):
    n = len(a)
    if n == 1:
        return 1
    
    max_i = 1

    for i in range(1, n):
        res = my_LIS(a[:i])
        if a[i - 1] < a[n - 1] and res >= max_i:
            max_i = res + 1
    
    return max_i


test_num = int(input())

for t in range(test_num):
    n = int(input())
    base_list = list(map(int, input().split()))    
    
    print('#' + str(t + 1) + ' ', end = '')
    print(my_LIS(base_list))