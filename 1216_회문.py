def isPalindrome(a):
    result = True
    for i in range(len(a) // 2):
        if a[i] != a[-i-1]:
            result = False
            break
    return result
for T in range(10):
    a = int(input())
    base_list = []  
    base_list_02 = [] 
    n = 100


    for i in range(n):
        base_list.append(list(input()))

    # print(base_list)

    for i in range(n):
        base_list_02.append([])
    

    for i in range(n):
        for j in range(n):
            base_list_02[i].append(base_list[j][i])

    # base_list02 = base_list(zip(*base_list))
    # print(base_list_02)

    # c b c a b b a c
    # b b a b c a b a
    # a b c b c c c a
    # b a c c a a b b
    # b c b c a c b c
    # c a b a c a c b
    # c a a a c c a b
    # c b a b a c a c

    max_length = 1
    for iterate_num in range(n):
        for i in range(n):
            temp_list = []
            for j in range(i+1, n+1):
                temp_list = base_list[iterate_num][i:j]
                if isPalindrome(temp_list) and len(temp_list) > max_length:
                    max_length = len(temp_list)
                    


    for iterate_num in range(n):
        for i in range(n):
            temp_list = []
            for j in range(i+1, n+1):
                temp_list = base_list_02[iterate_num][i:j]
                if isPalindrome(temp_list) and len(temp_list) > max_length:
                    max_length = len(temp_list)

    print(f'#{a} ' , end = '')
    print(max_length)

    
