for t in range(10):    
    n = 100
    base_list = []
    length_dict = {}
    num = int(input())
    #####   리스트 생성 - base_list
    for i in range(n):
        base_list.append([])

    for i in range(n):
        base_list[i] = list(map(int, input().split()))

    cnt = 0     #이동횟수를 저장할 변수 - 단 수직방향이동은 100으로 고정이므로 세지 않음

    # 시작 지점을 저장하는 딕셔너리(length_dict) 생성 - 나중에 cnt 세서 value로 저장할 용도
    for i in range(100):
        if base_list[0][i] == 1:
            length_dict[i] = 0


    for key in length_dict.keys():
        cnt = 0
        i = 0
        j = int(key)
        while i < 99:
            if j == 0:
                while base_list[i][j+1] != 0:
                        j += 1
                        cnt += 1
                i += 1
            elif j == 99:
                while base_list[i][j-1] != 0:
                        j -= 1
                        cnt += 1
                i += 1
            else:
                if base_list[i][j+1] == 1:
                    while base_list[i][j+1] != 0 and j != 99:
                        j += 1
                        cnt += 1
                        if j == 99:
                            break
                elif base_list[i][j-1] == 1:
                    while base_list[i][j-1] != 0 and j != 0:
                        j -= 1
                        cnt += 1
                        if j == 0:
                            break
                i += 1
        length_dict[key]= cnt

        a = min(list(value for value in length_dict.values()))
        
    print(f'#{t+1} ', end = '')
    for key, val in length_dict.items():
        if val == a:
            print(key)
        

  



