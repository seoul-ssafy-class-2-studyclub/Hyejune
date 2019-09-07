test_num = int(input())

for t in range(test_num):
    V, E = map(int,input().split())
    adj_list = []
    
    for i in range(V+1):
        adj_list.append([])
    
    for i in range(E):
        a, b = map(int,input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    S, G = map(int,input().split())

    cnt = 0
    flag = 0
    queue = [S]
    visited = [False]*(V+1)
    visited[S] = True
    while queue:
        if flag == 1:
            break
        cnt += 1
        for i in range(len(queue)):
            temp = queue.pop(0)
            for item in adj_list[temp]:
                if visited[item] == False:
                    if item == G:
                        flag = 1
                    queue.append(item)
                    visited[item] = True

    if flag == 0:
        cnt = 0
    print('#' + str(t+1) + ' ', end='')
    print(cnt)