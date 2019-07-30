
def changeColor(x):         # 인자로 받은 리스트에 해당하는 정보대로 색칠해주는 함수 정의
    for i in range(x[0], x[2] + 1):
        for j in range(x[1], x[3] + 1):
            if base_list[i][j] != 0 and base_list[i][j] != x[4]:
                base_list[i][j] = 7
            elif base_list[i][j] == 0:
                base_list[i][j] = x[4]

color_num = int(input())

for num in range(color_num):

    color_list_len = int(input())
    base_list = []
    color_list = []
    for i in range(10):
        base_list.append([0]*10)

    for i in range(color_list_len):
        color_list.append([])

    for i in range(color_list_len):
        color_list[i] = list(map(int, input().split()))

    for i in range(color_list_len):
        changeColor(color_list[i])

    result = 0
    for i in range(10):
        result += base_list[i].count(7)

    print('#' + str(num + 1) + ' ', end='')
    print(result)
