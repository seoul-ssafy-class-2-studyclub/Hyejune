test_num = int(input())


for t in range(test_num):

    N, M = map(int,input().split())
    base_list = []
    board = []

    for i in range(M):
        base_list.append(list(map(int,input().split())))

    for i in range(N):          # 칸을 색칠할 N*N짜리 보드 선언, 모든 칸을 0으로 초기화
        board.append([0]*N)

    for case in base_list:      # 주어진 조건에 따라 보드를 칠하기
        for i in range(N):
            for j in range(N):
                if case[0]-1 <= i < case[2] and case[1]-1 <= j < case[3]:
                    board[i][j] = 1


    cnt = 0                     # 칠해진 칸수를 저장할 변수 ==> 0으로 초기화
    for i in range(N):          # 보드를 돌며
        for j in range(N):
            if board[i][j] == 1:        # 칸이 칠해져있다면
                cnt += 1                # cnt를 1씩 증가시킴


    print('#' + str(t+1) + ' ',end='')
    print(cnt)
