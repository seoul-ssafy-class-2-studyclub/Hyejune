D = {1:-1, -1:1}

Gear = [0] * 4
for i in range(4):
    Gear[i] = list(input())

N = int(input())

move = [0] * N
for i in range(N):
    move[i] = list(map(int, input().split()))
    move[i][0] -= 1         # 인덱스 번호 헷갈리지 않도록 -1 해준다

# print(Gear)
# print(move)
def rotate(arr, d):
    if d == 1:
        temp = arr.pop()
        arr.insert(0,temp)
    if d == -1:
        temp = arr.pop(0)
        arr.append(temp)


def geargear(num, d, k, pre):
    if k == 4:
        return
    if k == 0:
        if num - 1 >= 0:
            if Gear[num][6] != Gear[num - 1][2]:    # 왼쪽거에 영향주는 경우
                geargear(num-1, D[d], k+1, num)

        if num + 1 < 4:
            if Gear[num][2] != Gear[num + 1][6]:    # 오른쪽에 영향주는 경우
                geargear(num+1, D[d], k+1, num)
                
        rotate(Gear[num], d)

    else:                   # 나를 돌아가게 한 톱니는 다시 돌리면 안된다
        if pre > num:       # 오른쪽에서 영향을 받아 돌아가므로 왼쪽만 보면된다.
            if num - 1 >= 0:
                if Gear[num][6] != Gear[num - 1][2]:    # 왼쪽거에 영향주는 경우
                    geargear(num-1, D[d], k+1, num)

        if pre < num:       # 왼쪽에서 영향을 받아 돌아가므로 오른쪽만 보면된다.
            if num + 1 < 4:
                if Gear[num][2] != Gear[num + 1][6]:    # 오른쪽에 영향주는 경우
                    geargear(num+1, D[d], k+1, num)

        rotate(Gear[num], d)


for i in range(N):
    geargear(move[i][0], move[i][1], 0, -1)

total = 0
mul_n = 1
for i in range(1,5):
    if Gear[i-1][0] == '1':
        total += mul_n
    mul_n *= 2

print(total)
