test_num =int(input())

def checkDup(arr):
    sp = -1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            sp = i
            break
    if sp == -1:
        return False
    else:
        arr = arr[:sp] + arr[sp+2:] 
        return arr

def deleteDup(arr):
    
    if checkDup(arr) == False:
        return arr
    else:
        return deleteDup(checkDup(arr))


for t in range(test_num):
    test_case = list(input())

    result = len(deleteDup(test_case))

    print('#' + str(t+1) + ' ', end='')
    print(result)
