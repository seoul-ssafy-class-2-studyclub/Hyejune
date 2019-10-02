N = int(input())
population = [0]
pupulation = list(map(int,input().split()))
# print(pupulation)
adj = [[] for i in range(N + 1)]
for i in range(N):
    temp = list(map(int,input().split()))
    adj[i+1] = temp[1:]

print(adj)
result_list = []
min_difference = 999999

def combi(k, arr, now, num):
    if k == num+1:
        result_list.append(arr)
        return
    else:
        for i in range(now+1, N+1):
            combi(k+1, arr + [i], i, num)

def connected(a,b):
    visited = [False] * (N + 1)
    visited[0] = True
    visited[a] = True
    queue = adj[a]
    while queue:
        temp = queue.pop(0)
        if temp == b:
            print('연결')
            return True
        if not visited[temp]:
            visited[temp] = True
            queue.extend(adj[temp])
    return False

def isit(arr):
    length = len(arr)
    if length == 1:
        return pupulation[arr[0]-1]
    else:
        sum_population = 0
        for i in range(1,length+1):
            sum_population += pupulation[arr[i]-1]
            for j in range(i+1,length+1):
                temp = connected(i,j)
                if temp == False:
                    return False
        
        return sum_population

if N % 2:
    x = N//2
else:
    x = N//2 + 1

for i in range(x+1):
    combi(0,[],0, i)

print(result_list)

while result_list:
    temp_top = result_list.pop(0)
    temp_bottom = result_list.pop()
    a = isit(temp_top)
    b = isit(temp_bottom)
    print(a,b)
    if a == False:
        continue
    if b == False:
        continue
    if min_difference > abs(a - b):
        min_difference  = abs(a - b)

print(min_difference)
    

