from pprint import pprint
test_num = int(input())

for t in range(test_num):
    N, M = map(int,input().split())
    board = [0]*N
    house_list = []
    for i in range(N):
        board[i] = list(map(int,input().split()))
        for j in range(N):
            if board[i][j] == 1:
                house_list.append((i,j))

    total_house_num = len(house_list)
    max_house = 0
    for i in range(N):
        for j in range(N):
            k = 0
            while True:
                temp_sum = 0
                house_cnt = 0
                k += 1
                for temp_i,temp_j in house_list:
                    if abs(temp_i - i) + abs(temp_j - j) < k:
                        temp_sum += M
                        house_cnt += 1
                if temp_sum - (k*k + (k-1)*(k-1)) >= 0:
                    if max_house < house_cnt:
                        max_house = house_cnt
                if house_cnt == total_house_num:
                    break
    print('#' + str(t+1) + ' ',end='')            
    print(max_house)