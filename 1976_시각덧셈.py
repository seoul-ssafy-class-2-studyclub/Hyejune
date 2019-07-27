test_case_num = int(input())
base_list = []

for i in range(test_case_num):
    base_list.append(list(map(int, input().split())))

for i in range(test_case_num):

    result_list = [0, 0]
    x = 0
    if base_list[i][1] + base_list[i][3] >= 60:
        result_list[1] = base_list[i][1] + base_list[i][3] - 60
        x = 1
    else:
        result_list[1] = base_list[i][1] + base_list[i][3]
    
    if base_list[i][0] + base_list[i][2] + x >= 12:
        result_list[0] = base_list[i][0] + base_list[i][2] - 12 + x
    else:
        result_list[0] = base_list[i][0] + base_list[i][2] + x

    print(f'#{i+1} {result_list[0]} {result_list[1]}')
    
