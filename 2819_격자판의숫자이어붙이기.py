test_num = int(input())
D = [(0,1), (0,-1), (1,0), (-1,0)]

for t in range(test_num):
    board = [0] * 4
    start = []
    queue = []
    visited = {}
    cnt = 0
    for i in range(4):
        board[i] = list(map(str,input().split()))

    def my_func(X):
        global result_list
        global cnt
        queue = [X]
        while queue:
            temp_x, temp_y, temp_z = queue.pop(0)
            if len(temp_z) == 7:
                if visited.get(temp_z) == None:
                    cnt += 1
                    visited[temp_z] = 1
                continue
            # if len(temp_z) == 7:
            #     if not temp_z in result_list:
            #         result_list.append(temp_z)
            #     continue
            for j in range(4):
                dx, dy = D[j]
                rx = temp_x + dx
                ry = temp_y + dy
                if 0 <= rx < 4 and 0 <= ry < 4:
                    # queue.append([rx,ry,temp_z*10+board[rx][ry]])
                    if queue == []:
                        queue = [[rx,ry,temp_z+board[rx][ry]]]
                        #0110111    
                        #0000011
                    else:
                        queue[-1:] = [queue[-1],[rx,ry,temp_z+board[rx][ry]]]
                    

    for x in range(4):
        for y in range(4):
            my_func([x,y,board[x][y]])
            
    
    print('#' + str(t+1) + ' ', end='')
    print(cnt)



# test_num = int(input())
# D = [(0,1), (0,-1), (1,0), (-1,0)]

# for t in range(test_num):
#     board = [0] * 4
#     start = []
#     queue = []
#     result_list = set()
#     for i in range(4):
#         board[i] = list(map(int,input().split()))

#     for i in range(4):
#         for j in range(4):
#             start += [(i,j)]

#     def my_func(X):
#         global result_list
#         queue = [X]
#         while queue:
#             temp_x, temp_y, temp_z = queue.pop(-1)
#             if len(str(temp_z)) == 7:
#                 result_list.add(temp_z)

#                 # if not temp_z in result_list:
#                 #     if result_list == []:
#                 #         result_list = [temp_z]
#                 #     else:
#                 #         result_list[-1:] = [result_list[-1],temp_z]
#                 continue
#             for j in range(4):
#                 dx, dy = D[j]
#                 rx = temp_x + dx
#                 ry = temp_y + dy
#                 if 0 <= rx < 4 and 0 <= ry < 4:
#                     if queue == []:
#                         queue = [[rx,ry,temp_z*10+board[rx][ry]]]
#                     else:
#                         queue[-1:] = [queue[-1],[rx,ry,temp_z*10+board[rx][ry]]]
                    

#     for item in start:
#         x, y = item
#         my_func([x,y,board[x][y]])
            
    
#     print('#' + str(t+1) + ' ', end='')
#     # print(result_list)
#     print(len(result_list))
