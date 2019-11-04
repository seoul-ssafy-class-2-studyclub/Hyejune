N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# # permutation
# visited = [False] * N
# # print(visited)

# min_result = 99999

# def per(arr, k, temp_sum):
#     global min_result
#     if k == N:
#         if temp_sum < min_result:
#             print(arr)
#             min_result = temp_sum
#         return
#     else:
#         for i in range(N):
#             if visited[i]:
#                 continue
#             visited[i] = True
#             sumsum = A[i]*B[k] + temp_sum
#             if sumsum < min_result:      # 이거 왜 안되지..
#                 per(arr + [A[i]], k+1, sumsum)
#             visited[i] = False

# per([], 0, 0)

# print(min_result)

A.sort(reverse=True)
B.sort()

sumsum = 0
for i in range(N):
    sumsum += A[i]*B[i]

print(sumsum)