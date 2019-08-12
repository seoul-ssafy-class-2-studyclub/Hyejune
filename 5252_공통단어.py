test_num = int(input())

for t in range(test_num):

    N, M = map(int, input().split())
    l_01 = []
    l_02 = []
    result = 0

    for i in range(N):
        l_01.append(input())

    for i in range(M):
        l_02.append(input())

    # print(l_01, l_02)

    for item in l_01:
        if item in l_02:
            result += 1

    print('#' + str(t+1) + ' ', end = '')
    print(result)