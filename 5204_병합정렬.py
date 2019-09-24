# 병합정렬
def merge(left, right):
    global cnt
    res = []
    if left[-1] > right[-1]:
        cnt += 1

    i = j = 0 #i , j  left, right 의 인덱스
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            if res == []:
                res = [right[j]]
            else:
                res[-1:] = [res[-1], right[j]]

            j += 1
        else:
            if res == []:
                res = [left[i]]
            else:
                res[-1:] = [res[-1], left[i]]

            i += 1
    
    if i < len(left):
        res.extend(left[i:])
    else:
        res.extend(right[j:])   

    return res

def sorting(arr):
    mid = len(arr) // 2

    if mid == 0: #arr의 길이가 0, 1이면 //2의 값이 2이므로
        return arr
    
    l = arr[:mid]
    r = arr[mid:]

    l = sorting(l)
    r = sorting(r)
    return merge(l, r)

for test_case in range(int(input())):
    N = int(input())
    test_arr = list(map(int,input().split()))
    cnt = 0
    test_arr = sorting(test_arr)
    print('#%d %d %d' %(test_case + 1, test_arr[N // 2], cnt))
