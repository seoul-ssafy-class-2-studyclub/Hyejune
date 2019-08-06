test_num = int(input())
A = [i for i in range(1, 13)]


for t in range(test_num):
    N, K = map(int, input().split())

    new_list = []
    result_list = []

    for i in range(1<<12):
        new_list.append([])
        for j in range(len(A)):
            if i & (1<<j):
                new_list[i].append(A[j])
    
    for item in new_list:
        if len(item) == N and sum(item) == K:
            result_list.append(item)

    print('#' + str(t+1) + ' ', end = '')
    print(len(result_list))
