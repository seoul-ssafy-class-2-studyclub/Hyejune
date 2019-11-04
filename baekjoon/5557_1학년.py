# 조합론 - 시간초과남

N = int(input())

num_list = list(map(int, input().split()))

# visited = [False for i in range(N-1)]
cnt = 0
def per(k, temp_res):
    global cnt
    if k == N-1:
        if temp_res == num_list[-1]:
            cnt += 1
        return
    else:
        # if num_list[k] == 0:
        #     per(k+1, temp_res)
        # else:
        for i in range(2):
            if i == 0:
                new_res = temp_res + num_list[k]
                if new_res <= 20:
                    per(k+1, new_res)
            else:
                new_res = temp_res - num_list[k]
                if 0 <= new_res:
                    per(k+1, new_res)

per(0, 0)
print(cnt)