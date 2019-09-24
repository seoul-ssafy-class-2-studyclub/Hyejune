# 순열로는 너무 오래걸린다 ㅎ 
test_num = int(input())

for t in range(test_num):

    N, M = map(int,input().split()) # N은 짐개수, M은 트럭 대수
    weight_list = list(map(int,input().split()))
    limit_list = list(map(int,input().split()))

    weight_list.sort(reverse=True)
    limit_list.sort(reverse=True)

    for i in range(len(limit_list)):
        if weight_list[i]

    max_res = 0
    # visited = [False] * N
    # def per(k, temp_res):
        
    #     global max_res
    #     if k == M or k == N:
    #         print(temp_res)
    #         if temp_res > max_res:
    #             max_res = temp_res
    #         return
    #     else:
    #         for i in range(N):
    #             if visited[i]:
    #                 continue
    #             visited[i] = True
    #             if limit_list[k] >= weight_list[i]:
    #                 per(k+1, temp_res + weight_list[i])
    #             else:
    #                 per(k+1, temp_res)
    #             visited[i] = False

    # per(0,0)



    print('#' + str(t+1) + ' ',end='')
    print(max_res)