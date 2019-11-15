route0 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0]
route1 = [0,2,4,6,8,10,13,16,19,25,30,35,40,0]
route2 = [0,2,4,6,8,10,12,14,16,18,20,22,24,25,30,35,40,0]
route3 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,28,27,26,25,30,35,40,0]

total_route = [route0,route1,route2,route3]

dice_num_list = list(map(int, input().split()))

piece_list = [[0,0],[0,0],[0,0],[0,0]]

max_result = 0
def dice(k, temp_result, temp_piece_list):
    global max_result
    if k == 10:
        print('마지막')
        if max_result < temp_result:
            max_result = temp_result
        return
    else:
        for i in range(4):
            new_piece_list = [0] * 4
            for m in range(4):
                new_piece_list[m] = temp_piece_list[m][:]

            current_route = new_piece_list[i][0]
            current_idx = new_piece_list[i][1]
            next_idx = current_idx + dice_num_list[k]       # 이 수가 각 루트의 경우 마지막 인덱스이거나 범위를 벗어났으면 piece_list의 해당 말에 -1표시
            # print(k, current_idx, next_idx)
            # print()
            if current_idx == -1:       # 도착점이거나 도착점을 지나친 말들은 -1로 표시해둠 -> 이경우에는 return
                return

            if current_route == 0:
                # 인덱스에러 나지 않도록 조건 주기
                if next_idx >= len(route0) - 1:
                    new_piece_list[i][1] = -1
                    dice(k+1, temp_result, new_piece_list)
                if current_idx == 5:
                    if [1,next_idx] in new_piece_list:
                        print('ㅠㅠㅠ')
                        return
                    new_piece_list[i][0] = 1    # route 1로 경로 변경
                    new_piece_list[i][1] = next_idx
                    print('음?')
                    dice(k+1, temp_result + route1[next_idx], new_piece_list)
                elif current_idx == 10:
                    if [2,next_idx] in new_piece_list:
                        # print('음????')
                        return
                    new_piece_list[i][0] = 2    # route 2로 경로 변경
                    new_piece_list[i][1] = next_idx
                    dice(k+1, temp_result + route2[next_idx], new_piece_list)
                elif current_idx == 15:
                    if [3,next_idx] in new_piece_list:
                        # print('음???????????')
                        return
                    new_piece_list[i][0] = 3    # route 3로 경로 변경
                    new_piece_list[i][1] = next_idx
                    dice(k+1, temp_result + route3[next_idx], new_piece_list)
                else:
                    if [0, next_idx] in new_piece_list:
                        return
                    new_piece_list[i][1] = next_idx
                    dice(k+1, temp_result + route0[next_idx], new_piece_list)
            else:
                if next_idx >= len(total_route[i]) - 1:
                    new_piece_list[i][1] = -1
                    dice(k+1, temp_result, new_piece_list)
                else:
                    if [current_route,next_idx] in new_piece_list:
                        # print('음???????????????????????')
                        return
                    new_piece_list[i][1] = next_idx
                    dice(k+1, temp_result + total_route[i][next_idx], new_piece_list)

dice(0,0,piece_list)

print(max_result)