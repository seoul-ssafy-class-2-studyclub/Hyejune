from pprint import pprint
# 격자판의 크기 R, C와 상어의 수 M
R, C, M = map(int,input().split())
aquarium = [0] * R
for i in range(R):
    aquarium[i] = [False]*C
shark_info = []

# (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
for i in range(M):
    shark_info.append(list(map(int,input().split())))

shark_idx = [0]*M
for i in range(M):
    shark_idx[i] = [shark_info[i].pop(0), shark_info[i].pop(0)]

pprint(shark_idx)
pprint(shark_info)

for i in range(M):              #인덱스가 1부터시작으로 문제에 나와있어서 1씩 차이남..
    aquarium[shark_idx[i][0]-1][shark_idx[i][1]-1] = i
pprint(aquarium)

def moveShark():
    for i in range(M):
        if shark_info[i][1] == 1:               # 위
            if shark_info[i][0] > shark_idx[i][0]:
                shark_idx[i][0] = shark_info[i][0] - shark_idx[i][0]
                shark_info[i][1] = 2
            else:
                shark_idx[i][0] -= shark_info[i][0]
        elif shark_info[i][1] == 2:             # 아래
            if shark_info[i][0] > R - shark_idx[i][0]:
                shark_idx[i][0] = shark_info[i][0] - R + shark_idx[i][0]
                shark_info[i][1] = 1
            else:
                shark_idx[i][0] += shark_info[i][0]
        elif shark_info[i][1] == 3:             # 오른쪽
            if shark_info[i][0] > C - shark_idx[i][1]:
                shark_idx[i][1] = shark_info[i][0] - C + shark_idx[i][1]
                shark_info[i][1] = 4
            else:
                shark_idx[i][1] += shark_info[i][0]
        elif shark_info[i][1] == 4:             # 왼쪽
            if shark_info[i][0] > shark_idx[i][1]:
                shark_idx[i][1] = shark_info[i][0] - shark_idx[i][1]
                shark_info[i][1] = 3
            else:
                shark_idx[i][1] -= shark_info[i][0]
    
moveShark()
moveShark()
print(shark_idx)
    
