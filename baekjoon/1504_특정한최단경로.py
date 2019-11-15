# 다익스트라 알고리즘

from heapq import heappush, heappop
N, E = map(int, input().split())



adj = [[] for i in range(N+1)]
for i in range(E):
    a, b, weight = map(int, input().split())
    adj[a].append((b,weight))
    adj[b].append((a,weight))

middle01, middle02 = map(int, input().split())

def dij(start,end):
    distance = [999999] * (N+1)
    distance[start] = 0

    queue = []
    heappush(queue, (0,start))

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

    return distance[end]

temp1 = dij(1,middle01) + dij(middle02,middle01) + dij(middle02,N)
temp2 = dij(1,middle02) + dij(middle01,middle02) + dij(middle01,N)

answer = min(temp1, temp2)
if answer >= 999999:
    answer = -1
print(answer)