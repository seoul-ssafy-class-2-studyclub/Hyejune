test_num = int(input())

for t in range(test_num):
    N, M = map(int,input().split())
    adj = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False] * (N + 1)
    visited[0] = True
    visited[1] = True

    cnt = 0
    queue = adj[1]
    
    def find():
        global queue
        for i in range(N+1):
            if visited[i] == False:
                queue.extend(adj[i])
                return
        return -1
    
    while True:
        cnt += 1
        while queue:
            temp = queue.pop(0)
            if visited[temp] == False:
                visited[temp] = True
                queue.extend(adj[temp])
        next_num = find()
        if next_num == -1:
            break

    print('#' + str(t+1) + ' ',end='')
    print(cnt)


