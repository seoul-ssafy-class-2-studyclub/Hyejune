from pprint import pprint

test_num = int(input())

adj = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]        # 주변 팔방을 조사하기 위한 배


for t in range(test_num):

    N = int(input())
    base_list = []
    cnt = 0
    
    
    for i in range(N):
        base_list.append(list(map(int,input().split())))

    # pprint(base_list)
    def FirstInx(arr):                      # 남아있는 섬인 부분을 찾아주는 함수 => 제일 처음 나오는 0보다 큰 수를 가진 인덱스반환 / 없으면 False반환
        sp_i = -1
        sp_j = -1
        for i in range(N):
            for j in range(N):
                if base_list[i][j] > 0:
                    sp_i = i
                    sp_j = j
                    return sp_i, sp_j
        return False


    def checkIsland(i,j):                   # i,j에 대해 그 주변을 조사하여 같은 섬인 땅을 같은 숫자로 표시해주는 함수
        base_list[i][j] = -(cnt+1)
        for [dx,dy] in adj:
            if 0 <= i+dx < N and 0 <= j+dy < N and base_list[i+dx][j+dy] > 0:
                base_list[i+dx][j+dy] = -(cnt+1)
                checkIsland(i+dx, j+dy)

    
    while True:
        if FirstInx(base_list) == False:
            break
        else:   
            (a, b) = FirstInx(base_list)
            checkIsland(a,b)
        cnt += 1

    
    # pprint(base_list)
        
    
    print('#' + str(t+1) + ' ',end='')
    print(cnt)
