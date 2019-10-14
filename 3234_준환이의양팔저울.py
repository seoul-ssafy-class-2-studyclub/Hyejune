# test_num = int(input())

# for t in range(test_num):
#     cnt = 0
#     result_list = []
#     N = int(input())
#     chuu = list(map(int,input().split()))

#     visited = [False] * N
#     cache = [-1] * (1 << N * 2)
    
#     print(visited)

#     def my_func(k,arr,left_sum,right_sum, now):
        
#         if cache[now] != -1:
#             return cache[now]
#         if k == N:
#             return 1
#         else:
#             res = 0
#             if left_sum == 0:
#                 # my_func(k+1, arr, left_sum, right_sum)
#                 res += my_func(k+1, arr, left_sum + arr[k], right_sum, now + (1 << (k - 1 + N)))
#             else:
#                 # my_func(k+1, arr, left_sum, right_sum)
#                 res += my_func(k+1, arr, left_sum + arr[k], right_sum, now + (1 << (k - 1 + N)))
#                 if left_sum >= right_sum + arr[k]:
#                     res += my_func(k+1, arr, left_sum, right_sum + arr[k], now + (1 << k - 1))
#         cache[now] = res
#         return res

#     def per(k, arr):
#         global visited
#         global result
#         if k == N:
#             # result_list.append(arr)
#             result += my_func(0,arr,0,0,0)
#             return
#         else:
#             for i in range(N):
#                 if not visited[i]:
#                     visited[i] = True
#                     per(k+1, arr + [chuu[i]])
#                     visited[i] = False
    
#     result = 0
#     per(0, [])
#     # print(result_list)

#     # for p in result_list:
#     #     my_func(0,p)

#     print('#' + str(t+1) + ' ', end='')
#     print(result)



# 힘들었다... 까먹지 말자
test_num = int(input())

for t in range(test_num):
    N = int(input())
    choo = list(map(int,input().split()))

    visited = [False] * N
    cache = [-1] * (1 << (N * 2))

    def per(k,left_sum, right_sum, now):


        if k == N:
            return 1

        if cache[now] != -1:
            return cache[now]

        else:
            res = 0
            for i in range(N):
                if not visited[i]:
                    visited[i] = True
                    res += per(k+1, left_sum + choo[i], right_sum, now + (1 << (i+N)))
                    if right_sum + choo[i] <= left_sum:
                        res += per(k+1, left_sum, right_sum + choo[i], now + (1 << i))
                    visited[i] = False
        cache[now] = res
        return res


    result = 0
    result = per(0,0,0,0)

    print('#' + str(t + 1) + ' ',end = '')
    print(result)
