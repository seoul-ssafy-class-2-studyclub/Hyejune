from heapq import heappop, heappush

INF = float('inf')
queue = []

heappush(queue, (0, 10))
heappush(queue, (5, 2))
heappush(queue, (3, 20))

print(heappop(queue))
print(heappop(queue))
print(heappop(queue))