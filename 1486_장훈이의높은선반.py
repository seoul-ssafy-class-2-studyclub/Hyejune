test_num = int(input())

for t in range(test_num):

    N, B = map(int, input().split())
    height = list(map(int,input().split()))
    min_difference = 9999

    def comb(k, now, sum_h):
        global min_difference
        if k == N or sum_h >= B:
            if abs(sum_h - B) < min_difference:
                min_difference = abs(sum_h - B)
            return
        else:
            for i in range(now+1, N):
                comb(k+1, i, sum_h + height[i])

            

    comb(0, -1, 0)


    print('#' + str(t+1) + ' ', end='')
    print(min_difference)