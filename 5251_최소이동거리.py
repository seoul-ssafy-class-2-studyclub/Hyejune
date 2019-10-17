
# 다익스트라 알고리즘 적용 문제

test_num = int(input())

for t in range(test_num):
    N, E = map(int, input().split())
    min_result = 999999
    adj = [0] * (N+1)
    weight_list = [{} for i in range(N+1)]
    for i in range(E):
        a, b, w = map(int, input().split())
        weight_list[a][b] = w

    # print(adj)
    # print(weight_list)

    visited = [False for i in range(N+1)]
    distance = [99999999999 for i in range(N+1)]
    distance[0] = 0

    
    while True:
        min_dist = 99999999999
        current_idx = -1

        if visited[N] == True:
            break

        for i in range(N+1):
            if not visited[i] and min_dist > distance[i]:
                current_idx = i
                min_dist = distance[i]
        
        visited[current_idx] = True

        for key, val in weight_list[current_idx].items():
            if not visited[key] and distance[key] > min_dist + val:
                distance[key] = min_dist + val

    print('#' + str(t+1) + ' ',end='')
    print(distance[N])



    
        


    # print('#' + str(t+1) + ' ', end='')
    # print(min_result)
    