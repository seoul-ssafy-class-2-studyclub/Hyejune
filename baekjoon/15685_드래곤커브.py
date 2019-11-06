D = {0:(0,1), 1:(-1,0), 2:(0,-1), 3:(1,0)}
N = int(input())

base_list = []

for i in range(N):
    base_list.append(list(map(int,input().split())))

result_list = []

def my_func(k, arr, d, g):          # 메인함수 --> K:몇번째 재귀로 들어왔는지, arr: 해당 드래곤 커브에 포함된 좌표, d:방향, g: 세대
    # print(arr)
    if k == g+1:            # 0세대부터 시작하므로 k가 g+1이 되었을때 재귀 탈출
        result_list.extend(arr)
    else:
        if k == 0:
            temp_i, temp_j = arr[0]
            di, dj = D[d]
            my_func(k+1, arr + [(temp_i + di, temp_j + dj)], d, g)
        else:
            temp_arr = arr[:]
            pivot = arr[-1]
            for i in range(2, len(arr)+1):
                temp_arr.append(secondary_func(arr[-i], pivot))
            my_func(k+1, temp_arr, d, g)

def secondary_func(targ , piv):
    p1, p2 = piv
    t1, t2 = targ
    return (p1+t2-p2, p2+p1-t1)

for i in range(N):
    my_func(0, [(base_list[i][1], base_list[i][0])], base_list[i][2], base_list[i][3])      # base_list에 저장된 처음 받아온 인풋을 차례로  

# print(result_list)
dragon_map = [ [0] * 101 for _ in range(101) ]
for res in result_list:
    dragon_map[res[0]][res[1]] = 1

def count_dragon(i, j):
    global cnt
    if dragon_map[i][j] == 1 and dragon_map[i + 1][j] and dragon_map[i][j + 1] and dragon_map[i + 1][j + 1]:
        cnt +=1

cnt = 0
for i in range(100):
    for j in range(100):
        count_dragon(i, j)

print(cnt)