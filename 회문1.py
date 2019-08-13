def isPal(arr):  # 주어진 문자열이 회문인지 확인하여 맞으면 Trud, 아니면 False반환하는 함수
    for i in range(len(arr)//2):
        flag = 0
        if arr[i] != arr[-1-i]:
            flag = -1
            break
    if flag == -1:
        return False
    else:
        return True

# print(isPal([1,1,2,1,1]))

for t in range(10):
    result = 0
    N = int(input())
    base_list = []
    base_list_02 = []
    for i in range(8):
        base_list.append(list(input()))

    # print(base_list)

    for i in range(8):
        for j in range(8+1-N):
            if isPal(base_list[i][j:j+N]) == True:
                # print(base_list[i][j:j+N])
                result += 1
        
            # print(i, j, result)
    

    for i in range(8):
        base_list_02.append([])
        for j in range(8):
            base_list_02[i].append(base_list[j][i])

    # print(base_list_02)

    for i in range(8):
        for j in range(8+1-N):
            if isPal(base_list_02[i][j:j+N]) == True:
                # print(base_list[i][j:j+N])
                result += 1
            # print(i, j, result)




    print('#' + str(t+1) + ' ', end = '')
    print(result)