# 틀림 - 왜틀렸는지 모르겠음

num, E, W, S, N  = map(float, input().split())

num = int(num)
E = E/100
W = W/100
S = S/100
N = N/100

D_probability = [E, W, S, N]
D = [(0,1), (0,-1), (1,0), (-1,0)]


# print(E, W, S, N)

result = 0
def my_func(temp_i, temp_j, k, temp_res, vis):
    global result
    if k == num:
        result += temp_res
        return
    else:
        new_vis = [0] * (2*num + 1)
        for a in range(2*num + 1):
            new_vis[a] = vis[a][:]

        for i in range(4):
            di, dj = D[i]
            ri = temp_i + di
            rj = temp_j + dj
            if not new_vis[ri][rj]:
                new_vis[ri][rj] = True
                my_func(ri, rj, k+1, temp_res * D_probability[i], new_vis)
            

visited = [[False for j in range(2*num + 1)] for i in range(2*num + 1)]
visited[num][num] = True


my_func(num, num, 0, 1, visited)
# result = sum(res_list)
# print('%0.9f'%(result))

print(result)