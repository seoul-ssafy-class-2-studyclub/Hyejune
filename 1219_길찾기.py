# 

for i in range(10):
    N, K = map(int, input().split())
    original_list = list(map(int, input().split()))
    arr_01 = [-1] * 100
    arr_02 = [-1] * 100 
    result = 0
    for i in range(K * 2):
        if not i % 2:   # 짝수면 ==> 인덱스는 0부터 시작하므로
            if arr_01[original_list[i]] == -1:
                arr_01[original_list[i]] = original_list[i+1]
            else:
                arr_02[original_list[i]] = original_list[i+1]
    b = False
    # print(arr_01)
    # print(arr_02)
    def searchPath(num):
        global b
        if num == 99:
            b = True
            return True
        else:
            for i in range(2):
                if i == 0 and arr_01[num] != -1:
                    if b:
                        return True
                    # print('arr_01[num]'+ str(arr_01[num]))
                    searchPath(arr_01[num])
                elif i == 1 and arr_02[num] != -1:
                    if b:
                        return True
                    # print('arr_02[num]'+ str(arr_02[num]))
                    searchPath(arr_02[num])
                
                

    # print(searchPath(0))
    if searchPath(0) == True:
        result = 1

    print('#' + str(N) + ' ', end='')
    print(result)



