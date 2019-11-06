# BFS, visited 둬야함, graph -> adj로 바꿔서 사용함

# from pprint import pprint

N = int(input())

original_graph = [0] * N
adj = [[] for i in range(N+1)]
for i in range(N):
    original_graph[i] = list(map(int, input().split()))
    for j in range(N):
        if original_graph[i][j] == 1:
            adj[i].append(j)

# print(adj)
result_graph = [[0 for j in range(N)] for i in range(N)]


for i in range(N):
    for j in range(N):
        queue = [i]
        visited = [False for a in range(N+1)]
        visited[i] = True
        flag = 0
        while queue:
            if flag == 1:
                break
            temp_node = queue.pop()
            for next_node in adj[temp_node]:
                if next_node == j:
                    result_graph[i][j] = 1
                    flag = 1
                    break
                if visited[next_node]:
                    continue
                visited[next_node] = True
                queue.append(next_node)

# pprint(result_graph)

for i in range(N):
    for j in range(N):
        print(result_graph[i][j], end=' ')
    print()