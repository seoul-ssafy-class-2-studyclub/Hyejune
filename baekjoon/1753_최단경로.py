# 다익스트라 알고리즘

# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
from heapq import heappush, heappop
V, E = map(int, input().split())

start = int(input())

adj = [[] for i in range(V+1)]
for i in range(E):
    a, b, weight = map(int, input().split())
    adj[a].append((b,weight))


distance = [999999] * (V+1)
distance[start] = 0

# print(adj)
# print(distance)

queue = []
heappush(queue, (0,start))

# print(queue)

while queue:
    temp_d, temp_idx = heappop(queue)

    if temp_d > distance[temp_idx]:
        continue

    for item in adj[temp_idx]:
        target_idx, target_d = item
        temp = temp_d + target_d
        if temp < distance[target_idx]:
            distance[target_idx] = temp
            heappush(queue, (temp, target_idx))

for i in range(1, V+1):
    if distance[i] == 999999:
        print('INF')
    else:
        print(distance[i])
        
