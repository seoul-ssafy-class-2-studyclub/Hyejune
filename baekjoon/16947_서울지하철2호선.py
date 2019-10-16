import sys
sys.setrecursionlimit(10000)




N = int(input())
adj = [[] for i in range(N+1)]
tran_point = set()
flag = -1
for i in range(1,N+1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    if len(adj[a]) > 2:
        tran_point.add(a)
    if len(adj[b]) > 2:
        tran_point.add(b)
    
# print(adj)
# print(tran_point)

circle_list = []
distance = []
def isCircle(origin,now,k,v,arr):
    global flag
    global circle_list
    global distance

    if k == 0:
        temp = v[:]
        temp[origin] = 0
        for i in range(len(adj[origin])):
            isCircle(origin, adj[origin][i], k+1, temp, arr + [adj[origin][i]])

    else:
        temp = v[:]
        temp[now] = 0
        if k > 1:
            if origin in adj[now]:
                flag = 1
                # if circle_list == []:
                circle_list = arr
                # if distance == []:
                distance = temp
                return
        for i in range(len(adj[now])):
            if temp[adj[now][i]] == -1:
                # temp[adj[now][i]] = 0
                if flag == -1:
                    isCircle(origin, adj[now][i], k+1, temp, arr + [adj[now][i]])

def findDistance(num, cnt):
    distance[num] = cnt
    if len(adj[num]) == 1:
        return
    for n in adj[num]:
        if distance[n] == -1:
            findDistance(n, cnt + 1)



for i in range(1, N+1):
    visited = [-1 for i in range(N+1)]
    isCircle(i,0,0,visited,[i])
    if flag == 1:
        break

# print(circle_list)
# print(distance)

for item in tran_point:
    findDistance(item, 0)

# print(distance)

for i in range(1, N+1):
    print(distance[i], end=' ')
