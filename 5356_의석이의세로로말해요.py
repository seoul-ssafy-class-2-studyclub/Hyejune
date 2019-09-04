from pprint import pprint
test_num = int(input())

for t in range(test_num):
    board = [0]*5
    max_length = 0
    for i in range(5):
        board[i] = list(input())
        temp = len(board[i])
        if temp > max_length:
            max_length = temp
    
    for i in range(5):
        l = len(board[i])
        if l == max_length:
            continue
        for j in range(max_length - l):
            board[i].append('-1')

    print('#' + str(t+1) + ' ',end='')
    for i in range(max_length):
        for j in range(5):
            temp = board[j][i]
            if temp == '-1':
                continue
            print(temp,end='')
    print()
    
    
        
    
    
