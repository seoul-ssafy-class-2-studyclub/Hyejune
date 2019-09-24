N, M, D = map(int,input().split())

board = [0]*N

for i in range(N):
    board[i] = list(map(int, input().split()))

max_cnt = 0

def my_func(k, arr, now):
    if k == 3:
        for item in arr:
            
        return
    else:
        for i in range(now+1, N):
            my_func(k+1, arr + [i], i)

my_func(0,[],-1)

# while True:
#     cnt = 0
#     if 1 in board[-1]:
#         break
        

