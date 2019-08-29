test_num = int(input())

for t in range(test_num):
    N, M = map(int,input().split())
    base_list = list(map(int,input().split()))
    
    print('#' + str(t+1) + ' ', end='')
    print(base_list[M%N])