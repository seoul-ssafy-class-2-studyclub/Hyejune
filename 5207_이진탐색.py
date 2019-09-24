test_num = int(input())

def binary_search(target, start_idx, end_idx,before):
    global cnt
    pivot = (start_idx + end_idx) // 2
    if start_idx > end_idx:
        return

    if target == a_list[pivot]:
        cnt += 1
        return
    elif target < a_list[pivot] and before in [0, 1]:
        binary_search(target, start_idx, pivot - 1, 2)
    elif target > a_list[pivot] and before in [0, 2]:
        binary_search(target, pivot + 1, end_idx, 1)




for t in range(test_num):
    N, M = map(int, input().split())
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))
    cnt = 0
    a_list.sort()
    for target in b_list:
        binary_search(target,0,N - 1,0)
    print('#%d %d' %(t + 1, cnt))