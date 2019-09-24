test_num = int(input())

def qsort(arr):
    global goal

    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    middle = []
    ll = 0
    lm = 0
    lr = 0

    for num in arr:
        if num < pivot:
            if left == []:
                left = [num]
            else:
                left[-1:] = [left[-1], num]
            ll += 1
        
        elif num == pivot:
            if middle == []:
                middle = [num]
            else:
                middle[-1:] = [middle[-1], num]
            lm += 1
        
        elif num > pivot:
            if right == []:
                right = [num]
            else:
                right[-1:] = [right[-1], num]
            lr += 1

    if ll > goal :
        return qsort(left)

    elif lm + ll > goal:
        goal -= ll
        return middle

    else:
        goal -= ll + lm
        return qsort(right)


for t in range(test_num):
    N = int(input())
    base_arr = list(map(int,input().split()))
    
    goal = N//2
    print('#' + str(t+1) + ' ', end = '')
    print(qsort(base_arr)[goal])