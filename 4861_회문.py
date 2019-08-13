def isPal(arr):  # 주어진 리스트가 회문인지 확인하여 맞으면 리스트, 아니면 False반환하는 함수
    for i in range(len(arr)//2):
        flag = 0
        if arr[i] != arr[-1-i]:
            flag = -1
            break
    if flag == -1:
        return False
    else:
        return arr

test_num = int(input())

for t in range(test_num):
    N, M = map(int, input().split())
    base_list = []
    base_list_02 = []
    for i in range(N):              # 기본 행렬 만들기
        base_list.append(list(input()))

    # print(base_list)

    for i in range(N):              # 세로로 찾기 편하도록 i, j위치 바꾼 행렬을 하나더 만들기
        base_list_02.append([])
        for j in range(N):
            base_list_02[i].append(base_list[j][i])
    
    # print(base_list_02)

    for i in range(N):
        for j in range(N-M+1):
            # print(base_list[i][j:j+M+1])
            if isPal(base_list[i][j:j+M+1]) != False:
                result = isPal(base_list[i][j:j+M+1])
                break
            elif isPal(base_list_02[i][j:j+M+1]) != False:
                result = isPal(base_list_02[i][j:j+M+1])
                break


    
    print('#' + str(t+1) + ' ', end='')
    print(''.join(map(str,result)))