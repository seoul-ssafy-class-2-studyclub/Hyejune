from pprint import pprint
test_num = int(input())

for t in range(test_num):
    N, M, K = map(int,input().split())
    board = [0]*N
    for i in range(N):
        board[i] = [0]*N
    original = [0]*K
    for i in range(K):
        original[i] = list(map(int,input().split()))
    # pprint(original)
    location = [0]*K
    status = [0]*K
    for i in range(K):
        location[i] = [original[i].pop(0),original[i].pop(0)]
        status[i] = original[i]

    # pprint(board)
    # print(location)
    # print(status)

    def changeLocation():           # 위치(location)를 바꿈
        for i in range(K):
            if status[i] == []:
                continue
            elif status[i][1] == 1:
                location[i][0] -= 1
            elif status[i][1] == 2:
                location[i][0] += 1
            elif status[i][1] == 3:
                location[i][1] -= 1
            elif status[i][1] == 4:
                location[i][1] += 1

    def changeStatus():             # 상태(status)를 바꿈
        for i in range(K):
            if location[i][0] == 0 or location[i][1] == 0 or location[i][0] == N-1 or location[i][1] == N-1:
                status[i][0] = status[i][0]//2
                if status[i][1] == 1:
                    status[i][1] = 2
                elif status[i][1] == 2:
                    status[i][1] = 1
                elif status[i][1] == 3:
                    status[i][1] = 4
                elif status[i][1] == 4:
                    status[i][1] = 3
        for a in range(K-1):
            if status[a] == []:
                continue
            temp_list = [[a,status[a][0]]]
            total = status[a][0]
            for b in range(a+1,K):
                if status[b] == []:
                    continue
                if location[a] == location[b]:
                    temp_list.append([b,status[b][0]])
                    total += status[b][0]
            # if len(temp_list) > 1:
            #     print(temp_list)
            if len(temp_list) > 1:
                max_num = 0
                for i in range(len(temp_list)):
                    if temp_list[i][1] > max_num:
                        max_num = temp_list[i][1]
                for i in range(len(temp_list)):
                    if temp_list[i][1] != max_num:
                        status[temp_list[i][0]] = []
                    else:
                        status[temp_list[i][0]][0] = total

    for i in range(M):
        changeLocation()
        changeStatus()

    result = 0
    for i in range(K):
        if status[i] == []:
            continue
        result += status[i][0]

    print('#' + str(t+1) + ' ', end='')
    print(result)
