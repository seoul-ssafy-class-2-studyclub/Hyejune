def my_max(a):                  # 최대값을 구하는 함수 my_max 정의
    max_int = a[0]
    for i in a:
        if i > max_int:
            max_int = i
    return max_int

for test_num in range(10):
    cnt = 0
    list_length = int(input())
    base_list = []
    base_list = list(map(int, input().split()))
    for i in range(2, list_length-1):
        if base_list[i] > base_list[i+1] and base_list[i] > base_list[i+2] and base_list[i] > base_list[i-1] and base_list[i] > base_list[i-2]:
            cnt += base_list[i] - max(base_list[i+1], base_list[i+2], base_list[i-1], base_list[i-2])
    
    print(f'#{test_num+1} ', end='')
    print(cnt)



