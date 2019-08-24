test_num = int(input())

for t in range(test_num):
    n = int(input())
    base_list = []
    harvest_list = list(i for i in range(1,n+1) if i%2)
    
    for i in range(n//2):
        harvest_list.append(harvest_list[n//2 -1 - i])

    # print(harvest_list)


    for i in range(n):
        base_list.append(list(map(int,input())))

    # print(base_list)

    harvest_list02 = []

    # for i in range(n//2 + 1):
    #     harvest_list02.append(base_list[i][n//2-i:n//2+1+i])

    # for i in range(n//2):
    #     harvest_list02.append(base_list[n//2+1+i][n//2-(n-i)-1:n//2+(n-i)-2])

    for i in range(n):
        harvest_list02.append(base_list[i][n//2 - harvest_list[i]//2 : n//2 + harvest_list[i]//2 + 1])

    # print(harvest_list02)

    result = 0
    for i in range(n):
        result += sum(harvest_list02[i])
    
    print('#' + str(t + 1) + ' ', end = '')
    print(result)