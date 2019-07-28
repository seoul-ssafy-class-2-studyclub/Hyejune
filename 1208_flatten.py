# x = [1, 10, 4, 5]

def Dump(a):
    a[a.index(max(a))] -= 1
    a[a.index(min(a))] += 1
    return a

def findDifference(a):
    return max(a) - min(a)

# print(Dump(x))



for test_num in range(10):
    dump_num = int(input())
    base_list = []
    base_list = list(map(int, input().split()))
    
    for i in range(dump_num):
        base_list = Dump(base_list)
        
    print(f'#{test_num+1} {findDifference(base_list)}')
