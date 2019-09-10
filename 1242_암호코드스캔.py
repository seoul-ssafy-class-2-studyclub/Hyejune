from pprint import pprint
base_dict = {'0':'0001101','1':'0011001','2':'0010011','3':'0111101','4':'0100011','5':'0110001','6':'0101111','7':'0111011','8':'0110111','9':'0001011'}
test_num = int(input())

for t in range(test_num):
    N, M = map(int, input().split())
    board = [0 for i in range(N)]
    for i in range(N):
        board[i] = list(input())

    print(board)