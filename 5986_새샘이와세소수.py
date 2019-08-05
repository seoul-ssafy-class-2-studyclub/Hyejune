# 2~ 999사이의 소수를 저장한 배열 구하기
prime_list = [2]
for i in range(3,1000,2):   # 2 초과 100미만 홀수 중
    check = 0
    for j in range(3, i//3+1):
        if i % j ==0:
            check = -1
            break
    if check == 0:
        prime_list.append(i)

# print(prime_list)


test_num = int(input())

for t in range(test_num):
    N = int(input())
    result_list = []
    cnt = 0
    for a in range(len(prime_list)): 
        for b in range(a, len(prime_list)): 
            for c in range(b, len(prime_list)): 
                if prime_list[a] + prime_list[b] + prime_list[c] == N:
                    result_list.append([prime_list[a] , prime_list[b] , prime_list[c]])

    print('#' + str(t+1) + ' ', end = '')
    print(len(result_list))