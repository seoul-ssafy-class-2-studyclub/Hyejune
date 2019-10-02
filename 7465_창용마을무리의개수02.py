test_num = int(input())

def find(num):
    for item in adj[num]:
        if not visited[item]:
            visited[item] = True
            find(item)


for t in range(test_num):
    N, M = map(int,input().split())
    adj = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False] * (N + 1)
    visited[0] = True
    cnt = 0

    
    for i in range(1,N+1):
        if not visited[i]:
            cnt += 1
            visited[i] = True
            find(i)

    print('#' + str(t+1) + ' ',end='')
    print(cnt)
