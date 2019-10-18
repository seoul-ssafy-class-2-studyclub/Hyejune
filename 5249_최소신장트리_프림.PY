from heapq import heappop, heappush

test_num = int(input())

for t in range(test_num):
    V, E = map(int,input().split())
    adj = [{} for i in range(V+1)]
    for i in range(E):
        v1, v2, w = map(int,input().split())
        adj[v1][v2] = w
        adj[v2][v1] = w

    # print(adj)

    queue = []
    heappush(queue,(0,0))       # 앞에 있는게 가중치

    weight_list = [999999999 for i in range(V+1)]
    weight_list[0] = 0

    visited = [False for i in range(V+1)]


    while queue:
        temp_weight, temp_node = heappop(queue)
        visited[temp_node] = True

        for key, val in adj[temp_node].items():
            if visited[key]:
                continue
            if weight_list[key] > val:
                weight_list[key] =  val
                heappush(queue, (weight_list[key], key))


    print('#' + str(t+1) + ' ',end='')
    print(sum(weight_list))