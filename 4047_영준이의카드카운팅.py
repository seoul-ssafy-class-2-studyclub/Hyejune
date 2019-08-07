test_num = int(input())

for t in range(test_num):
    original_list = input()
    base_list = []
    # print(original_list)
    for i in range(len(original_list)//3):
        base_list.append(original_list[3*i:3*(i+1)])
    
    # print(base_list)
    s_list = []
    c_list = []
    h_list = []
    d_list = []
    check = 1
        
    for card in base_list:
        if card[0] =='S':
            if not card[1:] in s_list:
                s_list.append(card[1:])
            else:
                check = -1
        elif card[0] =='C':
            if not card[1:] in c_list:
                c_list.append(card[1:])
            else:
                check = -1
        elif card[0] =='H':
            if not card[1:] in h_list:
                h_list.append(card[1:])
            else:
                check = -1
        elif card[0] =='D':
            if not card[1:] in d_list:
                d_list.append(card[1:])
            else:
                check = -1
                
      
    s_result = 13 - len(s_list)
    d_result = 13 - len(d_list)
    h_result = 13 - len(h_list)
    c_result = 13 - len(c_list)

    print('#' + str(t+1) + ' ', end = '')
    if check == 1:
        print(str(s_result) + ' ' + str(d_result) + ' ' + str(h_result) + ' ' + str(c_result))
    else:
        print('ERROR')