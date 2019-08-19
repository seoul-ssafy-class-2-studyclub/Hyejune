# 

for i in range(10):
    N, K = map(int, input().split())
    visited = [False] * 100
    original_list = list(map(int, input().split()))
    origin_set = set(original_list)
    result = 0
    adjacent_list = []
    for i in range(100):
        adjacent_list.append([])
    
    for i in range(0, len(original_list), 2):
        # if i % 2 == 0:
        adjacent_list[original_list[i]].append(original_list[i+1])
        # else:
        #     adjacent_list[original_list[i]].append(original_list[i-1])

    for i in range(len(adjacent_list)):
        adjacent_list[i].reverse()

    # print(adjacent_list)

    stack = [0]
    result = 0

    while stack:
        # if visited.count(True) == len(origin_set):
        #     result = 0
        #     break
        temp = stack.pop()
        if temp == 99:
            result = 1
            break

        if visited[temp] == False:
            visited[temp] = True
            stack += adjacent_list[temp]
                
    

    print('#' + str(N) + ' ', end='')
    print(result)



