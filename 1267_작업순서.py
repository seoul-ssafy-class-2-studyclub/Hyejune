for t in range(10):
    V, E = map(int, input().split())

    original_list = list(map(int, input().split()))
    adjacent_list = []  # 인접리스트 선언
    new_list = []
    visited = [False] * (V+1)
    

    for i in range(V+1):
        adjacent_list.append([])

    for i in range(len(original_list)):
        if not i % 2:
            adjacent_list[original_list[i]].append(original_list[i+1])
        else:
            new_list.append(original_list[i])
    
    result_node = []        # 최종결과 저장할 리스트
    for i in range(1, V+1):         # 들어오는 간선이 없는 노드들을 시작노드로 설정 (미리 result_node에 넣어두기)
        if not i in new_list:
            result_node.append(i)
        
    stack = []              # 스택으로 사용할 리스트
    for item in result_node:        
        stack += adjacent_list[item]
        adjacent_list[item] =[]
    while stack:
        l_list = []
        for i in range(len(adjacent_list)):
            l_list += adjacent_list[i]

        temp = stack.pop()

        if visited[temp] == False:
            visited[temp] = True
            
            if temp not in l_list:
                result_node.append(temp)
                stack += adjacent_list[temp]
                adjacent_list[temp] = []
            else:
                stack.insert(0,temp)
                visited[temp] = False

    print('#' + str(t+1) + ' ', end='')
    print(' '.join(map(str, result_node)))