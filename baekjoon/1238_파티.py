# 다익스트라 응용 or 플로이드 와샬

from heapq import heappush, heappop

N, M ,X = map(int, input().split())

adj = [{} for i in range(N+1)]

for i in range(M):
    a, b, t = map(int, input().split())
    adj[a][b] = t

# print(adj)

result_table = [{} for i in range(N+1)]

def dijkstra(a):
    weight_list = [999999 for i in range(N+1)]
    weight_list[0] = 0
    weight_list[a] = 0
    queue = []
    heappush(queue, (0,a))

    while queue:
        temp_weight, temp_idx = heappop(queue)

        if temp_weight > weight_list[temp_idx]:
            continue

        for key, val in adj[temp_idx].items():
            temp = temp_weight + val
            if weight_list[key] > temp:
                weight_list[key] = temp
                heappush(queue, (temp, key))

    for i in range(N + 1):
        result_table[a][i] = weight_list[i]

for i in range(1, N+1):
    dijkstra(i)

# print(result_table)

max_result = 0

for i in range(1, N+1):
    temp = result_table[i][X] + result_table[X][i]
    if temp > max_result:
        max_result = temp

print(max_result)
