from pprint import pprint
import sys
sys.setrecursionlimit(10000)
# from pprint import pprint

I, J = map(int,(input().split()))       # 가로길이, 세로길이 인풋받기

base_list = []          # 보드로 사용할 리스트 선언
for i in range(I):      # 보드에 한줄씩 받기
    base_list.append(list(map(int,(input().split()))))
base_list[0][0] = 2

# 상하좌우 좌표 변화리스트
d_inx = [[0,1], [0,-1], [1,0], [-1,0]]
time = 0            # 치즈가 녹는데 걸린 시간을 담을 변수


# 바깥 공기를 전부 2로 바꾸어주는 함수 정의
def OuterAir(arr):
    for i in range(I):
        for j in range(J):
            for [dx, dy] in d_inx:
                if 0 <= i+dx < I and 0 <= j+dy < J and arr[i][j] == 2:
                    if arr[i+dx][j+dy] == 0:
                        arr[i+dx][j+dy] = 2
                        OuterAir(arr)
        


# 바깥공기와 접촉한 치즈를 녹이는 함수
def MeltCheese(arr):
    global time
    time += 1
    for i in range(I):
        for j in range(J):
            for [dx, dy] in d_inx:
                if 0 <= i+dx < I and 0 <= j+dy < J and arr[i][j] == 1:
                    if arr[i+dx][j+dy] == 2:
                        arr[i][j] = 3
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 3:
                arr[i][j] = 2
    return arr


# 남은 치즈 개수를 세는 함수
def CountCheese(arr):
    cnt = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 1:
                cnt +=1

    return cnt


# pprint(MeltCheese(base_list))
num_Cheese = []
while True:
    if num_Cheese != [] and num_Cheese[-1] == 0:
        break
    OuterAir(base_list)
    # pprint(base_list)
    print()
    MeltCheese(base_list)
    pprint(base_list)
    print()
    num_Cheese.append(CountCheese(base_list))
    
# print(num_Cheese)



print(time)
print(num_Cheese[-2])
