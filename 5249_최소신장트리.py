# Kruskal or Prim algorithm 적용 문제

test_num = int(input())

for t in range(test_num):
    V, E = map(int, input().split())
    parent = {}
    rank = {}
    result = 0

    # 노드를 독립적인 집합으로
    def makeSet(v):
        parent[v] = v
        rank[v] = 0

    # 해당 노드 최상의 노드 찾기
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])

        return parent[v]

    # 두 노드 연결
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)

        if root1 != root2:
            # 짧은 트리..? 작은트리..? 가 더 큰걸 가리키도록
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2

                if rank[root1] == rank[root2]:  
                    rank[root2] += 1

    def kruskal(graph):
        for v in graph['vert']:
            makeSet(v)

        mst = []
        global result

        edges = graph['edges']  # 이미 가중치 기준으로 소팅된 상태이므로 그냥 가져오기만한다

        for edge in edges:
            weight, v1, v2 = edge

            if find(v1) != find(v2):
                union(v1,v2)
                mst.append(edge)
                result += edge[0]

        return mst


    temp_list = [0] * E
    for i in range(E):
        a, b, c = list(map(int, input().split()))
        temp_list[i] = (c, a, b)

    # test = [(6,1,1), (3,2,5), (5,2,2)]
    # test = sorted(test)
    # print(test)

    temp_list = sorted(temp_list)
    graph = {
        'vert' : [i for i in range(0, V+1)],
        'edges' : temp_list
    }

    # print(kruskal(graph))
    kruskal(graph)
    print('#' + str(t+1) + ' ', end='')
    print(result)
    