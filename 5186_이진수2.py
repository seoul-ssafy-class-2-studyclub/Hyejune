test_num = int(input())

for t in range(test_num):
    num = float(input())

    compare = 0.5
    result_list = []
    flag = 0
    while True:
        if len(result_list) > 12:
            flag = 1
            break
        if num >= compare:
            result_list.append(1)
            num -= compare
            compare = compare /2
            if num == 0:
                break
        else:
            result_list.append(0)
            compare = compare / 2

        
    
    print('#' + str(t+1) + ' ',end='')
    if flag == 1:
        print('overflow')
    else:
        print(''.join(map(str,result_list)))