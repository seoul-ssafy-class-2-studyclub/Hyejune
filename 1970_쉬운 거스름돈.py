

testcase_num = int(input())
change_list = []
for i in range(testcase_num):
    change_list.append(int(input()))

for i in range(testcase_num):
    change = change_list[i]
    base_dict = {50000: 0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}

    for key, val in base_dict.items():
        base_dict[key] = change//key
        change -= key * (change//key)

    print(f'#{i+1}')
    for key, val in base_dict.items():
        print(f'{val} ', end=' ')
    print()

