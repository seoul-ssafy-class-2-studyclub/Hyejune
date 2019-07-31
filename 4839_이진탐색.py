test_num = int(input())

def searchBinary(p, target):
    l = 0
    r = len(p)-1
    cnt = 0
    while l <= r:
        mid = int((r + l) / 2)
        if p[mid] > target:
            r = mid
            cnt += 1
        elif p[mid] < target:
            l = mid
            cnt += 1
        else:
            cnt += 1
            break
    
    return cnt


for num in range(test_num):

    P, A, B = map(int, input().split())

    base_list = []
    for i in range(1,P+1):
        base_list.append(i)

    # print(searchBinary(base_list, A))
    # print(searchBinary(base_list, B))
    print('#' + str(num + 1) + ' ', end='')
    if searchBinary(base_list, A) < searchBinary(base_list, B):
        print('A')
    elif searchBinary(base_list, B) < searchBinary(base_list, A):
        print('B')
    else:
        print('0')