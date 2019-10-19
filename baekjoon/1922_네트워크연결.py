# 프림 알고리즘으로 mst 구성
from heapq import heappush, heappop

N = int(input())
M = int(input())

adj = [{} for i in range(N+1)]                # 0번째 인덱스는 안씀
for i in range(M):
    a, b, cost = list(map(int, input().split()))
    adj[a][b] = cost
    adj[b][a] = cost

# print(cost_list)
cost = [9999999 for i in range(N+1)]            # 0번째 인덱스는 안씀
cost[1] = 0

visited = [False for i in range(N+1)]               # 0번째 인덱스는 안씀

queue = [(0,1)]     # 현재까지 가중치합, 현재 노드

sum_result = 0
cnt = 0
while queue:
    # print(queue)
    
    current_cost, current_node = heappop(queue)
    # print(current_node)
    if visited[current_node]:        # 이거 중요
        continue

    visited[current_node] = True

    sum_result += current_cost
    for key, val in adj[current_node].items():
        if visited[key]:
            continue
        if cost[key] > val:
            cost[key] = val
            heappush(queue, (cost[key], key))
    


print(sum_result)




