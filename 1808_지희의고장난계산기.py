test_num = int(input())

for t in range(test_num):
    temp_list = list(map(int,input().split()))
    X = int(input())
    button_num = []
    min_press = -1
    
    for i in range(10):
        if temp_list[i] == 1:
            button_num.append(i)

    # def my_func(x,temp_cnt):
    #     temp_x = str(x)
    #     flag = 0
    #     for temp in temp_x:
    #         if flag == -1:
    #             break
    #         if not int(temp) in button_num:
    #             flag = -1
    #     if flag == -1:
    #         if x == 1:
    #             return 
    #         for i in range(2, int(X ** 0.5)):
    #             if x % i == 0:

    #     if temp_cnt < min_press:
    #         min_press = temp_cnt
    #     return

    my_func(X,3)

    # print(button_num)

    

    print('#' + str(t+1) + ' ',end='')
    print(min_press)