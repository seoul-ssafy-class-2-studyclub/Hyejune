# 위에 주석처리한 코드는 답은 나오지만 for문을 많이 돌아서 느리다

# def isIncreasingNum(n):
#     temp_list = list(map(int,list(str(n))))
#     check = 1

#     for i in range(1, len(temp_list)):
#         if temp_list[i] < temp_list[i - 1]:
#             check = -1
#             break

#     if check == -1:
#         return False
#     else:
#         return True

        

# test_num = int(input())

# for t in range(test_num):
#     l = int(input())
#     base_list = list(map(int, input().split()))

#     new_list = []

#     for i in range(l - 1):
#         for j in range(i+1, l):
#             new_list.append(base_list[i] * base_list[j])

    
#     result_list = []

#     for i in range(len(new_list)):
#         if isIncreasingNum(new_list[i]):
#             if len(result_list) == 0:
#                 ma = new_list[i]
#             elif ma < new_list[i]:
#                 ma = new_list[i]


#     print('#' + str(t+1) + ' ', end = '')
#     print(ma)


def monotonic(n):
    a = n % 10
    n = int(n / 10)
    while n != 0:
        if n % 10 > a:
            return False
        else:
            a = n % 10
            n = int(n / 10)
    return True

test_num = int(input())
for t in range(test_num):
    l = int(input())
    base_list = list(map(int, input().split()))
    result = -1
    for i in range(l - 1):
        for j in range(i+1, l):
            mul = base_list[i] * base_list[j]
            if mul < result:
                continue
            if monotonic(mul):
                result = mul
    print('#' + str(t+1) + ' ', end = '')
    print(result)

