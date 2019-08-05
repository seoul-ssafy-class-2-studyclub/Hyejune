
test_num = int(input())

for t in range(test_num):
    N = int(input())
    original_list = list(map(int, input().split()))     # 있는 그대로 받아오는 list
    base_list = []          # 두개씩 끊어서 저장하는 list

    for i in range(N):
        base_list.append([original_list[2*i], original_list[2*i +1 ]])
    

    new_list = [base_list[0]]
    base_list.pop(0)

    while base_list != []:
        for item in base_list:
            if item[0] == new_list[-1][-1]:
                new_list.append(item)
                base_list.remove(item)
            elif item[-1] == new_list[0][0]:
                new_list.insert(0,item)
                base_list.remove(item)

    print('#' + str(t+1) + ' ', end = '')
    for i in range(N):
        for j in range(2):
            print(new_list[i][j], end = ' ')
    print()


