# 순열은 visited를 둬야한다!
sample_list = ['a', 'b', 'c', 'd']

N = int(input())    # 뽑을 개수

result_list = []
visited = [False] * len(sample_list)

def per(k, arr):
    if k == N:
        result_list.append(arr)
        return
    else:
        for i in range(len(sample_list)):
            if visited[i]:
                continue
            visited[i] = True
            per(k+1, arr + [sample_list[i]])
            visited[i] = False

per(0,[])

print(result_list)

