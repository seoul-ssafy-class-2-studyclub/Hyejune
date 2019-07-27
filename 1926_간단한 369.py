num = int(input())
base_list = ['3', '6', '9']


for i in range (1, num+1):
    cnt = 0
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        for j in str(i):
            if j in base_list:
                cnt += 1
        print('-' * cnt, end=' ')

    else:
        print(i, end=' ')