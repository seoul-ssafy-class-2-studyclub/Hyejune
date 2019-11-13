test_num = int(input())
op = ['+', '-', '*', '/']

for t in range(test_num):
    N = int(input())

    operand_list = list(map(int, input().split()))

    num_list = list(map(int, input().split()))

    max_num = -999999
    min_num = 999999
    def dup_per(k, temp_res):
        global max_num
        global min_num
        if k == N-1:
            if temp_res > max_num:
                max_num = temp_res
            if temp_res < min_num:
                min_num = temp_res
            return
        else:
            for i in range(4):
                if operand_list[i] > 0:
                    operand_list[i] -= 1
                    
                    if i == 0:
                        next_res = temp_res + num_list[k+1]
                    elif i ==1:
                        next_res = temp_res - num_list[k+1]
                    elif i == 2:
                        next_res = temp_res * num_list[k+1]
                    elif i == 3:
                        if temp_res < 0:
                            next_res = -((-temp_res) // num_list[k+1])
                        else:
                            next_res = temp_res // num_list[k+1]
                    
                    dup_per(k+1, next_res)
                    operand_list[i] += 1

    dup_per(0, num_list[0])

    print('#' + str(t+1) + ' ', end='' )
    print(max_num - min_num)