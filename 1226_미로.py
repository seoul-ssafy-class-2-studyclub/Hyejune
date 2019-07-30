n = 16  # 16 * 16 행렬
for test_num in range(10):
    base_list = []
    num = int(input())  # 문제에서 주는 index 인풋값 - 의미없음

    #####   리스트 생성 - base_list
    for i in range(n):
            base_list.append(list(input()))

    
    # 도착지점의 좌표 찾아두기
    for i in range(n):
        for j in range(n):
            if base_list[i][j] =='3':
                end_i = i
                end_j = j


    check_num = 0
    # while check_num == 0:    이렇게는 못풀거같다..
        # for i in range(1, n-1):
        #     for j in range(1, n-1):
        #         if base_list[i][j] == 2:
        #             print(i,j)
        #             if base_list[i-1][j] == 0:     # 위
        #                 base_list[i-1][j] = 2
        #             elif base_list[i][j+1] == 0:    # 오른쪽
        #                 base_list[i][j+1] = 2
        #             elif base_list[i+1][j] == 0:    # 아래
        #                 base_list[i+1][j] = 2
        #             elif base_list[i][j-1] == 0:    # 왼쪽
        #                 base_list[i][j-1] = 2
        #             else:
        #                 check_num = -1

    for iterate in range(10):
        j = 1
        i = 1
        check_num = 0

        while check_num == 0:
            if check_num == -1:
                    break
            while i < n:
                if check_num == -1:
                    break
                while j < n:
                    if check_num == -1:
                        break
                    if i > 15 or j > 15:
                        break
                    if base_list[i][j] == '2':
                        # print(i,j)
                        if base_list[i-1][j] == '0':     # 위
                            base_list[i-1][j] = '2'
                            i -= 1
                        elif base_list[i][j+1] == '0':    # 오른쪽
                            base_list[i][j+1] = '2'
                            j +=1
                        elif base_list[i+1][j] == '0':    # 아래
                            base_list[i+1][j] = '2'
                            i += 1
                        elif base_list[i][j-1] == '0':    # 왼쪽
                            base_list[i][j-1] = '2'
                            j -= 1
                        else:
                            check_num = -1
                    
    for i in range(n):
        for j in range(n):
            print(base_list[i][j] + ' ', end = '')
        print()

    print('#' + str(test_num + 1) + ' ', end='')
    if base_list[end_i + 1][end_j] == '2' or base_list[end_i - 1][end_j] == '2' or base_list[end_i][end_j + 1] == '2' or base_list[end_i][end_j - 1] == '2':    # 3 주변에 2가 있나 체크해서 있으면 1프린트
        print('1')
    else:
        print('0')





