base = ['+', '-', '*', '/']

N = int(input())

num_list = list(map(int,input().split()))

temp_op = list(map(int,input().split()))

op = []
for i in range(4):
    op.extend([base[i]] * temp_op[i])

mi = 999999999999999999999
ma = -99999999999999999999
visited = [False] * len(op)

def per(k, temp_res):
    global mi 
    global ma
    if k == len(op):            #####
        if temp_res < mi:
            mi = temp_res
        if temp_res > ma:
            ma = temp_res
        return
    else:
        for i in range(len(op)):
            if visited[i] == True:
                continue
            visited[i] = True
            if op[i] == '+':
                temp = temp_res + num_list[k+1]
            elif op[i] == '-':
                temp = temp_res - num_list[k+1]
            elif op[i] == '*':
                temp = temp_res * num_list[k+1]
            elif op[i] == '/':
                temp = int(temp_res / num_list[k+1])
            per(k+1, temp)
            visited[i] = False

per(0, num_list[0])

print(ma)
print(mi)