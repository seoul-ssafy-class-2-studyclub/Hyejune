test_num = int(input())
for t in range(test_num):
    N = int(input())
    original_list = list(map(int,input().split()))
    comp1 = original_list[:]
    comp1.sort()
    comp2 = list(reversed(comp1))

    def shuffle(x,arr):         # x 값의 범위는 0 ~ N-1
        l = N//2
        temp_arr1 = arr[:l]
        temp_arr2 = arr[l:]
        result_list = []
        if l >= x:
            for i in range(l-x):
                    result_list.append(temp_arr1.pop(0))
            for i in range(l+x):
                if temp_arr2 != []:
                    result_list.append(temp_arr2.pop(0))
                if temp_arr1 != []:
                    result_list.append(temp_arr1.pop(0))
        else:
            for i in range(x-l+1):
                    result_list.append(temp_arr2.pop(0))
            for i in range(l+x-1):
                if temp_arr1 != []:
                    result_list.append(temp_arr1.pop(0))
                if temp_arr2 != []:
                    result_list.append(temp_arr2.pop(0))
        return result_list
    
    def perm(k, arr):
        global result
        if k < 6 and result == -1:
            for i in range(1,N):
                temp_arr = shuffle(i,arr)
                if temp_arr == comp1 or temp_arr == comp2:
                    print(k,i)
                    print(temp_arr)
                    result = k
                if result == -1:
                   perm(k+1, temp_arr)

    result = -1
    if original_list == comp1 or original_list == comp2:
        result = 0
    else:
        perm(1, original_list)

    print('#' + str(t+1) + ' ',end='')
    print(result)

# 1
# 4
# 4 2 3 1

