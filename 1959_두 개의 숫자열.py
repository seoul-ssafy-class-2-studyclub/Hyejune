
test_case_num = int(input())
final_result_list = []
for num in range(test_case_num):
    n, m = map(int, input().split())

    base_list_n = str(input()).split()
    base_list_m = str(input()).split()


    # print(base_list_n)
    # print(base_list_m)

    for i in range(abs(n - m)):
        if n > m :
            base_list_m.append('0')
        elif n < m:
            base_list_n.append('0') 

    result_list = []
    sum = 0
    for i in range(abs(m - n)+1):
        # print(base_list_n)
        # print(base_list_m)
        for j in range(max(m, n)):
            sum += int(base_list_n[j]) * int(base_list_m[j])
        result_list.append(sum)
        if n > m :
            base_list_m.insert(0,'0')
            base_list_m.pop()
        elif n < m :
            base_list_n.insert(0,'0')
            base_list_n.pop()
        sum = 0
        
    # print(result_list)
    final_result_list.append(max(result_list))

for i in range(test_case_num):
    print('#' + str(i + 1) + ' ' + str(final_result_list[i]))



# 테스트케이스형식
# 10
# 3 5
# 1 5 3
# 3 6 -7 5 4