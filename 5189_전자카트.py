from pprint import pprint
test_num = int(input())

# permutation 이용해서 info_list의 겹치는 j 가 없도록 i행에서 한개씩만 골라서 더하기, 그걸 result_list 에 저장했다가 최소를 result로 출력
for t in range(test_num):
    N = int(input())
    info_list = [0]*N
    visited = [False] * N
    result_list = []
    for i in range(N):
        info_list[i] = list(map(int, input().split()))

    # pprint(info_list) 
    

    def per(k,total,pre):
        if k == N-1:
            # print(pre,end=' ')
            # print('0',end=' ')
            # print(info_list[pre][0],total)
            result_list.append(total+info_list[pre][0])
            return
        else:
            for j in range(N):
                if visited[j] == True:
                    continue
                visited[j] = True
                # total += info_list[pre][j]
                # print(pre,j,info_list[pre][j],total)
                per(k+1,total+info_list[pre][j],j)
                visited[j] = False

    visited[0] = True
    per(0,0,0)
    result = min(result_list)

    print('#' + str(t+1) + ' ', end='')
    print(result)


