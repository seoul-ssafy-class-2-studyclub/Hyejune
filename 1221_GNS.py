my_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

test_num = int(input())

for t in range(test_num):
    n_list = list(input().split())
    base_list = list(input().split())
    new_list = []
    final_list = []

    for item in base_list:
        new_list.append(my_dict[item])

    new_list.sort()
    # print(new_list)

    for item in new_list:
        for key, val in my_dict.items():
            if item == val:
                final_list.append(key)
    print(f'#{t+1} ', end='')
    for i in range(len(final_list)):
        print(final_list[i], end = ' ')
