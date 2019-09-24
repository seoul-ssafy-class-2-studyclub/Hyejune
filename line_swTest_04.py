N = int(input())
seat = list(map(int,input().split()))

max_zero = 0

pointer = 0
temp = 0

while True:
    if seat[pointer] == 0:
        temp += 1
    elif seat[pointer] == 1:
        if temp > max_zero:
            max_zero = temp
        temp = 0
    pointer += 1
    if pointer == N:
        if temp > max_zero:
            max_zero = temp
        break

# print(max_zero)

if seat[0] == 0:
    flag = 0
    for i in range(1,max_zero):
        if seat[i] == 0:
            continue
        else:
            flag = -1
            break
    if flag == 0:
        result = max_zero

elif seat[-1] == 0:
    flag = 0
    for i in range(1,max_zero):
        if seat[-1-i] == 0:
            continue
        else:
            flag = -1
            break
    if flag == 0:
        result = max_zero

else:
    if max_zero % 2 == 0:
        result = max_zero // 2
    else:
        result =  max_zero // 2 + 1

print(result)