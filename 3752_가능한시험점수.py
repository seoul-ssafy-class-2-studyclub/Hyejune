test_num = int(input())

for t in range(test_num):
    N = int(input())
    base = list(map(int,input().split()))
    
    visited = [False] * (sum(base) + 1)
    cnt = 0
    cache = [{} for _ in range(N)]

    def my_func(k,temp):
        global cnt

        if k == N:
            if not visited[temp]:
                visited[temp] = True
                cnt += 1
            return
        
        if cache[k].get(temp) == 1:
            return
        
        my_func(k+1, temp)
        my_func(k+1, temp + base[k])
        cache[k][temp] = 1
        
    

    my_func(0,0)
    print(cache)
    print('#' + str(t+1) + ' ', end='')
    print(cnt)


# test_num = int(input())

# for t in range(test_num):
#     N = int(input())
#     base = list(map(int, input().split()))
#     cnt = 0
#     cache = [{} for i in range(N)]
#     visited = [False] * (sum(base) + 1)

#     def my_func(k,temp):
#         global cnt
#         if k == N:
#             if not visited[temp]:
#                 visited[temp] = True
#                 cnt += 1
#             return
        
#         if cache[k].get(temp) == 1:
#             return

#         my_func(k+1, temp)
#         my_func(k+1, temp + base[k])
#         cache[k][temp] = 1

#     my_func(0,0)

#     print('#' + str(t+1) + ' ', end='')
#     print(cnt)