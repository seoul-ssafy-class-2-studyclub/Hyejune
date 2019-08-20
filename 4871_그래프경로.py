test_num =int(input())

for t in range(test_num):
    
    V, E = map(int,(input().split()))
    # graph = []
    # for i in range(V+1):
    #     graph.append([0]*(V+1))
    # # print(graph)

    # for i in range(E):
    #     a, b = map(int,(input().split()))
    #     graph[a][b] = 1

    # for i in range(V+1):
    #     print(graph[i])

    # 인접리스트 만들기

    adjacent_list = []
    for i in range(V+1):
        adjacent_list.append([])
    for i in range(E):
        a, b = map(int,(input().split()))
        adjacent_list[a].append(b)
    # print(adjacent_list)

    sp, ep = map(int,(input().split()))

    stack = [sp]
    visited = [False] * (V + 1)
    result = 0

    while stack:
        temp = stack.pop()

        if temp == ep:
            result = 1
            break
        if visited[temp] == False:
            visited[temp] = True
            stack += adjacent_list[temp]
    


    print('#' + str(t+1) + ' ', end='')
    print(result)


