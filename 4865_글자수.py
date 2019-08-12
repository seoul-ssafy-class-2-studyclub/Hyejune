test_num = int(input())

for t in range(test_num):
    l_01 = list(set(input()))
    l_02 = list(input())
    result = 0
    new_list = [0]*len(l_02)
    final_list = [0]*len(l_01)

    for item in l_01:
        for i in range(len(l_02)):
            if item == l_02[i]:
                new_list[i] = item

    for i in range(len(l_01)):
        final_list.append(new_list.count(l_01[i]))

    result = max(final_list)
    
    print('#' + str(t+1) + ' ', end = '')
    print(result)