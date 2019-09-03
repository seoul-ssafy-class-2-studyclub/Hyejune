# 시간초과

N = int(input())

base_list = list(map(int,input().split()))
result_list = []
max_num = 0

gap = (base_list[-1] - base_list[0]) // 2

for i in range(1,gap+1):
    visited = [False] * len(base_list)
    for j in range(len(base_list)):
        base = base_list[j] 
        if visited[j]:
            continue
        visited[j] = True
        if ( base + i) not in base_list:
            continue
        visited[base_list.index(base+i)] = True
        if ( base + 2*i) not in base_list:
            continue
        visited[base_list.index(base+2*i)] = True
        temp = 3 * (base+i)
        cnt = 3
        arr = [base, base+i, base+2*i]
        while base + (cnt * i) in base_list:
            temp += cnt*i + base
            visited[base_list.index(base+cnt*i)] = True
            arr += [base+cnt*i]
            cnt += 1
        if max_num < temp:
            max_num = temp
            # result_list.append(temp)
        # print(arr)
print(max_num)
        