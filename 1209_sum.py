
for t in range(10):
    test_num = int(input())
    n = 100
    base_list = []      #가로 계산용 리스트
    base_list_02 = []   #세로 계산용 리스트
    sum_list = []       # sum결과 저장용 리스트

    for i in range(n):  #리스트 내 리스트 생성
        base_list.append([])
        base_list_02.append([])
    
    for i in range(n):  #가로 리스트 생성 & 가로 계산결과 append
        base_list[i] = list(map(int, input().split()))
        sum_list.append(sum(base_list[i]))

    for i in range(n):  #세로 리스트 생성            
        for j in range(n):
            base_list_02[i].append(base_list[j][i])
        
    for i in range(n):
        sum_list.append(sum(base_list_02[i]))       #세로 계산결과 append

    c_sum01 = 0
    c_sum02 = 0
    for i in range(n):
        c_sum01 += base_list[i][i]
        c_sum02 += base_list[i][-1-i]

    sum_list.append(c_sum01)
    sum_list.append(c_sum02)

    print(f'#{t+1} {max(sum_list)}')

# 4 4 3 2 1
# 2 2 1 6 5
# 3 5 4 6 7
# 4 2 5 9 7
# 8 1 9 5 6
    