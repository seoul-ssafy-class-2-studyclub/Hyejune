test_num = int(input())

for t in range(test_num):

    base_list = list(map(int,input().split()))
    N = base_list.pop(0)
    min_cnt = 99999

    def refill(battery, k, cnt):
        global min_cnt
        if k == N - 1:
            if min_cnt > cnt:
                min_cnt = cnt
            return
        else:
            if cnt >= min_cnt:
                return
            # for i in range(2):
                # if i == 0:  # k 번째를 안고른다
            if battery > 0 :
                refill(battery - 1, k + 1, cnt)
                # elif i == 1:    # k 번째를 고른다
            refill(base_list[k] - 1, k + 1, cnt + 1 )


    refill(base_list[0] - 1, 1, 0)

    print('#' + str(t+1) + ' ', end='')
    print(min_cnt)