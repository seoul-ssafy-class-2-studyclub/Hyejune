def my_sort(arr):                       # 내림차순 정렬 함수 정의
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def my_max(a):                  # 최대값을 구하는 함수 my_max 정의
    max_int = a[0]
    for i in a:
        if i > max_int:
            max_int = i
    return max_int

def isitDone(arr):          # 지금상태가 내림차순인경우 최종결과 리스트를 반환하는 함수 아니면 False 리턴
    temp_arr = arr[:]
    if arr == my_sort(temp_arr):
        if N % 2 == 0:
            result_list = base_list
            return result_list
        else:
            if len(arr) == len(set(temp_arr)):           # 중복되는게 없으면 마지막꺼 두개 바꿔주기
                temp = base_list[-2]
                base_list.pop(-2)
                base_list.append(temp)
                result_list = base_list
                return result_list
            else:
                result_list = base_list
                return result_list 
    else:
        return False

# a = [6, 9, 2, 4, 5]
# print(my_sort(a))


test_num = int(input())

for t in range(test_num):
    base_list, N = input().split()
    base_list = list(map(int, base_list))
    N = int(N)
    result_list = []

    new_list = []

    if isitDone(base_list) == False:
        while N > 0:
            # print()
            # print('while' + str(N))
            if isitDone(base_list) != False:
                # print('if에 들어옴')
                result_list = isitDone(base_list)
                break
            elif base_list[0] == my_max(base_list):
                # print('elif에 들어옴')
                new_list.append(base_list[0])
                base_list.pop(0)
            else:
                # print('else에 들어옴')
                temp_arr2 = list(reversed(base_list))
                if base_list.count(my_max(base_list)) != 1:         # 중복 max존재, 제일뒤에 값을 뽑아야함
                    # print('else 의 if에 들어옴')
                    if N == 1:                                      # 남은 바꾸기 횟수가 1인경우
                        max_idx = temp_arr2.index(my_max(base_list))
                        base_list[0], base_list[-max_idx-1] = base_list[-max_idx-1], base_list[0]
                        N -= 1
                    else:
                        l_01 = []
                        how_many_max = base_list.count(my_max(base_list))
                        how_many_rest = len(base_list) - how_many_max
                        temp_n = min(N, how_many_max, how_many_rest)        
                        for item in base_list:
                            if len(l_01) == temp_n:
                                break
                            if item != my_max(base_list):
                                l_01.append(item)
                                base_list[base_list.index(item)] = -1
                        my_sort(l_01)
                        for i in range(temp_n):
                            base_list[base_list.index(-1)] = my_max(base_list)
                        for i in range(temp_n):
                            temp_arr2 = list(reversed(base_list))
                            max_idx = temp_arr2.index(my_max(base_list))
                            base_list[-max_idx-1] = l_01[-1]
                            l_01.pop(-1)
                        N -= temp_n
                        
                    # print(max_idx)
                    # print(new_list, end='')
                    # print(base_list)
                else:
                    # print('else 의 else에 들어옴')
                    max_idx = base_list.index(my_max(base_list))
                    base_list[0], base_list[max_idx] = base_list[max_idx], base_list[0]
                    N -= 1
                    # print(new_list, end='')
                    # print(base_list)
    else:
        result_list = isitDone(base_list)

    if base_list != []:
        result_list = new_list + base_list
    # result_list = new_list + result_list



    


    print('#' + str(t+1) + ' ', end = '')
    print(''.join(map(str, result_list)))