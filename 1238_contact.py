for t in range(10):
    L, start = map(int,input().split())
    adj_list = []
    for i in range(101):
        adj_list.append([])
    original = list(map(int,input().split()))
    for i in range(0,L,2):
        adj_list[original[i]].append(original[i+1])
    
    queue = [start]
    visited = [False]*101

    cnt = 1
    visited[start] = cnt
    result_list = []
    while queue:
        cnt += 1
        temp_list = []
        for i in range(len(queue)):
            temp = queue.pop(0)

            for item in adj_list[temp]:
                if visited[item] == False:
                    queue.append(item)
                    visited[item] = cnt
                    temp_list.append(item)
        result_list.append(temp_list)
                    

    # print(visited)
    # print(result_list)
    result = max(result_list[-2])

    print('#' + str(t+1) + ' ', end='')
    print(result)