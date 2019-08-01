punc_list = ['!', '?', '.']
test_num = int(input())

for t in range(test_num):
    base_list = list(map(str, input().split()))

    cnt = 0
    for i in range(len(base_list)):
        if base_list[i][0:1].isupper():
            if base_list[i][1:].islower() or (base_list[i][1:-1].islower() and base_list[i][-1] in punc_list ) or len(base_list[i])==1:
                cnt += 1
            

    

    # print('#' + str(t + 1) + ' ', end='')
    # print(result)