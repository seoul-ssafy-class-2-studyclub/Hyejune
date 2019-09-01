M = int(input())
N = int(input())

distance_list = list(map(int,input().split()))
repair_time_list = list(map(int,input().split()))
result_list = []
min_num = 9999
visit = []

def repair(k,arr, d, t):
    global min_num
    global visit
    if k == N:
        if t < min_num:
            min_num = t
            visit = arr
            # result_list.append([arr,t])
        return
    else:
        for i in range(2):
            if i == 0:           # k번째 인덱스의 정비소에 방문하는 경우
                repair(k+1,arr+[k+1],0,t+repair_time_list[k])               # 정비소 인덱스가 1부터 시작하므로 +1해준다
            else:           # k 번째 인덱스의 정비소에 방문하지 않는 경우
                if d + distance_list[k] + distance_list[k+1] > M:
                    return
                else:
                    repair(k+1,arr,d+distance_list[k],t)

repair(0,[],0,0)

print(min_num)
print(len(visit))
print(' '.join(map(str,visit)))

        

