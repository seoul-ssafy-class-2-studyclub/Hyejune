base_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
test_num = int(input())

for t in range(test_num):
    N, base = input().split()
    N = int(N)
    base = list(base)
    
    print('#' + str(t+1) + ' ',end='')
    for i in range(N):
        temp_val = base_dict[base[i]]
        temp_list = []
        for j in range(4):
            temp_list.append(temp_val%2)
            temp_val = temp_val//2
        temp_list.reverse()
        print(''.join(map(str,temp_list)),end='')
    print()
        
