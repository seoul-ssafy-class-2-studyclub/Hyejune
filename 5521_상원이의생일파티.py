test_num = int(input())

for t in range(test_num):
    N, M = map(int,input().split())

    adj = [[] for i in range(N+1)]

    for i in range(M):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)

    # print(adj)
    visited = [False for i in range(N+1)]
    visited[1] = True
    queue = [1]
    friend_num = 0
    cnt = 0

    while queue:
        if cnt == 2:
            break
        cnt += 1
        for i in range(len(queue)):
            temp = queue.pop(0)
            for friend in adj[temp]:
                if not visited[friend]:
                    visited[friend] = True
                    friend_num += 1
                    queue.append(friend)

    print('#' + str(t+1) + ' ',end='')
    print(friend_num)