test_num = int(input())

for t in range(test_num):
    min_price = 99999

    fee = list(map(int,input().split()))

    plan = list(map(int,input().split()))

    def per(k, temp_sum):
        global min_price
        if k >= 12:
            if min_price > temp_sum:
                min_price = temp_sum
            return
        else:
            if plan[k] == 0:
                per(k+1, temp_sum)
            else:
                per(k+1, temp_sum + (plan[k] * fee[0]))
                per(k+1, temp_sum + fee[1])
                per(k+3, temp_sum + fee[2])
                if k == 0:
                    per(k+12, temp_sum + fee[3])

    per(0,0)
    print('#' + str(t+1) + ' ', end='')
    print(min_price)