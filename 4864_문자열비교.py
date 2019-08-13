def isIn(arr1, arr2):
    N = len(arr1)
    M = len(arr2)

    for i in range(M-N+1):
        if arr1 == arr2[i:i+N]:
            return True
    return False


# print(isIn('123', '1112311'))

test_num = int(input())

for t in range(test_num):
    result = 0
    l_01 = input()
    l_02 = input()

    if isIn(l_01, l_02) == True:
        result = 1
    
    print('#' + str(t+1) + ' ', end='')
    print(result)