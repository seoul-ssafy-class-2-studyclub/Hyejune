test_num = int(input())

for t in range(test_num):
    N = int(input())
    base_list = []

    while len(base_list) != N:
        base_list += list(map(int, input().split()))

    base_list02 = ''.join(map(str,base_list))
    check = -2

    # print(base_list)
    # print(base_list02)

    for i in range(10):
        if not i in base_list:
            num = check = i
            break

    if check == -2:
        num = 10
        while check == -2:
            if base_list02.find(str(num)) == -1:
                break
            num += 1
            
    print('#' + str(t+1) + ' ', end = '')
    print(num)