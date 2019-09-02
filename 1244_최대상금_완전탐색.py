test_num = int(input())

for t in range(test_num):
    original, N = input().split()
    N = int(N)
    l = len(original)
    chache = [{} for _ in range(N + 1)]
    result = 0

    def changeCard(k,num):
        if k == N:
            return num
        
        if chache[k].get(num) != None:
            res = chache[k][num]
            return res
        
        res = 0
        for i in range(0,l-1):
            for j in range(i+1,l):
                temp = list(num)
                new_temp = ''
                temp[i], temp[j] = temp[j], temp[i]
                for o in range(l):
                    # print(temp)
                    new_temp += temp[o]
                # new_temp = int(new_temp)
                res = max(res,int(changeCard(k+1,new_temp)))
        res = str(res)

        chache[k][num] = res

        return res
    
        
    result = changeCard(0,original)
    print('#' + str(t+1) + ' ',end='')
    print(int(result))



# new = ''
#     for i in range(l):
#         new += original[i]
#     new = int(new)
#     print(type(new))

# a = 123
# a = list(str(a))
# print(a)