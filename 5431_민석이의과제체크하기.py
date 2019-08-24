test_num = int(input())

for t in range(test_num):
    N, k = map(int, input().split())
    submit_list = list(map(int, input().split()))

    result_list = []

    for i in range(1, N+1):
        if not i in submit_list:
            result_list.append(i)

    print('#' + str(t + 1) + ' ', end = '')
    print(' '.join(map(str,result_list)))