test_num = int(input())

for t in range(test_num):
    N = int(input())
    base_list = [0 for i in range(N)]
    for i in range(N):
        base_list[i] = list(map(int,input().split()))

    min_num = 9999999
    visited = [False for i in range(N)]

    def per(k, sum_price):
        global min_num
        if k == N:
            if min_num > sum_price:
                min_num = sum_price
            return
        else:
            if sum_price >= min_num:
                return
            for i in range(N):
                if visited[i] == False:
                    visited[i] = True
                    per(k+1, sum_price + base_list[k][i])
                    visited[i] = False

    per(0, 0)
    print('#' + str(t+1) + ' ', end = '')
    print(min_num)