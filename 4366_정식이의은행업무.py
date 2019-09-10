test_num = int(input())

for t in range(test_num):
    binary = list(input())
    ternary = list(input())

    def BToD(num):
        result = 0
        for i in range(len(num)):
            result += (2 ** i) * int(num[-i-1])
        return result
    
    def TToD(num):
        result = 0
        for i in range(len(num)):
            result += (3 ** i) * int(num[-i-1])
        return result

    b_result_list = []
    t_result_list = []

    for i in range(len(binary)):
        temp_binary = binary[:]
        if binary[i] == '0':
            temp_binary[i] = '1'
            b_result_list.append(BToD(temp_binary))
        elif binary[i] == '1':
            temp_binary[i] = '0'
            b_result_list.append(BToD(temp_binary))

    for i in range(len(ternary)):
        temp_ternary = ternary[:]
        if ternary[i] == '0':
            temp_ternary[i] = '1'
            t_result_list.append(TToD(temp_ternary))
            temp_ternary[i] = '2'
            t_result_list.append(TToD(temp_ternary))
        elif ternary[i] == '1':
            temp_ternary[i] = '0'
            t_result_list.append(TToD(temp_ternary))
            temp_ternary[i] = '2'
            t_result_list.append(TToD(temp_ternary))
        elif ternary[i] == '2':
            temp_ternary[i] = '0'
            t_result_list.append(TToD(temp_ternary))
            temp_ternary[i] = '1'
            t_result_list.append(TToD(temp_ternary))
        

    answer = 0
    for item in b_result_list:
        if item in t_result_list:
            answer = item
            break

    print('#' + str(t+1) + ' ',end='')
    print(answer)
    
    