test_num = int(input())

for t in range(test_num):
    N, L = map(int, input().split())
    info_list = [0]*N
    for i in range(N):
        info_list[i] = list(map(int,input().split()))

    max_score = 0

    def hamburger(k,c,score):        # k는 깊이(depth), c는 지금까지의 칼로리, score는 지금까지의 점수
        global max_score
        if k == N:
            if score > max_score:
                max_score = score
            return
        else:
            for i in range(2):
                if i == 0:
                    hamburger(k+1,c,score)
                elif i == 1:
                    if c + info_list[k][1] > L:
                        return
                    else:
                        hamburger(k+1, c + info_list[k][1], score + info_list[k][0])


    hamburger(0,0,0)
    print('#' + str(t+1)+ ' ',end='')
    print(max_score)