

for t in range(10):
    result_list = []
    V, E = map(int, input().split())
    original_list = list(map(int, input().split()))
    new_list = []
    for i in range(E):
        new_list.append([original_list[i*2], original_list[i*2+1]])

    # print(original_list)
    # print(new_list)

    for i in range(1, V+1):                 # 끝나는 숫자 (V) 구하기
        if i == new_list[i-1][0]:
            continue
        end = i
    print(end)


    # print('#' + str(t+1) + ' ', end='')
    # print(result_list)