import random

arr = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
    ]

# arr = []
# for i in range(5):
#     arr.append([])
#     for j in range(5):
#         arr[i].append(random.randint(0,100))

dx = [0,0,1,-1]
dy = [-1,1,0,0]

for i in range(len(arr)):
    print(arr[i])
print()

# print(result_list)
def my_side(arr):
    result_list = []
    for i in range(5):
        r=[]
        for j in range(5):
            r.append(0)
        result_list.append(r)
    

    for x in range(len(arr)):
        sum = 0
        for y in range(len(arr[x])):
            sum = 0
            for i in range(4):
                test_x = x + dx[i]
                test_y = y + dy[i]
                if test_x >= 0 and test_x <=4 and test_y >= 0 and test_y <=4:
                    sum += abs(arr[x][y] - arr[test_x][test_y])
            result_list[x][y] = sum
    return result_list

for i in range(len(arr)):
    print(my_side(arr)[i])
