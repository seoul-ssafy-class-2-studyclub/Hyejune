def print_pascal(x):
    pascal_list = []
    pascal_len = x
    for i in range(pascal_len):
        pascal_list.append([])


    for i in range(pascal_len):

        for j in range(i+1):
            if j == 0 or j == i:
                pascal_list[i].append(1)
            else:
                pascal_list[i].append(pascal_list[i-1][j] + pascal_list[i-1][j-1])


    for i in range(pascal_len):
        for j in pascal_list[i]:
            print(j, end=' ')
        print()


test_num = int(input())

for t in range(test_num):
    N = int(input())

    print('#' + str(t+1))
    print_pascal(N)