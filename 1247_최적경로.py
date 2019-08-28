test_num = int(input())


def distance(s1,s2):
    return abs(s1[0]-s2[0]) + abs(s1[1]-s2[1])

for t in range(test_num):
    N = int(input())

    original = list(map(int,input().split()))
    start = []
    end = []
    customer = [0]*N
    visited = [False]*N
    min_total = 999999
    for i in range(2):
        start.append(original.pop(0))
    for i in range(2):
        end.append(original.pop(0))
    for i in range(N):
        customer[i] = [original.pop(0), original.pop(0)]

    def min_distance(k,total,xy):
        global min_total
        if k == N:
            temp = total + distance(xy,end)
            if temp < min_total:
                min_total = temp
        else:
            for i in range(N):
                if visited[i]:
                    continue
                if total > min_total:
                    continue
                visited[i] = True
                total += distance(xy,customer[i])
                min_distance(k+1,total,customer[i])
                visited[i] = False
                total -= distance(xy,customer[i])           #여기 꼭 적어줘야함

    # print(start, end)
    # print(customer)
    min_distance(0,0,start)
    print('#' + str(t+1) + ' ', end='')
    print(min_total)