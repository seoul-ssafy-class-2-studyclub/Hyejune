from pprint import pprint
N = int(input())

base_list = []
adj = [[0,1], [0,-1], [1,0], [-1,0]]
cnt = 0
house_num = 1
result_list = []

for i in range(N):
    base_list.append(list(map(int,list(input()))))


def FirstInx(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                return i, j
    return False

def checkApt(i,j):
    global house_num
    base_list[i][j] = -(cnt+1)
    for [dx, dy] in adj:
        if 0 <= i+dx < N and 0 <= j+dy < N and base_list[i+dx][j+dy] > 0:
            base_list[i+dx][j+dy] = -(cnt+1)
            house_num += 1
            checkApt(i+dx, j+dy)
        
while True:
    if FirstInx(base_list) == False:
        break
    else:
        (a, b) = FirstInx(base_list)
        checkApt(a,b)
        pprint(base_list)
    result_list.append(house_num)
    house_num = 1
    cnt += 1

sorted(result_list)
print(cnt)
for item in result_list:
    print(item)


    

