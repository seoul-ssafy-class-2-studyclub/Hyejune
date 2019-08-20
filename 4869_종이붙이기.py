

def Paper(length):
    memo_list = [0, 1, 3]
    L = length//10
    # if length == 0:
    #     return 1

    if L < len(memo_list):
        return memo_list[L]

    else:
        for i in range(len(memo_list), L+1):
            memo_list.append(memo_list[i-1] + memo_list[i-2]*2)

    return memo_list[L]



test_num = int(input())

for t in range(test_num):
    N = int(input())
    print('#' + str(t+1) + ' ', end = '')
    print(Paper(N))
