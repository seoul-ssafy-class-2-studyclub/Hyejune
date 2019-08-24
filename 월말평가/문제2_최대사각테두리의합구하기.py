
test_num = int(input())

def OuterSum(arr):              # 주어진 이차원배열의 테두리 수 합을 구하는 함수 정의
    s = 0
    s += sum(arr[0])
    s += sum(arr[-1])

    for i in range(1, len(arr)-1):
        s += arr[i][0]
        s += arr[i][-1]
    return s


for t in range(test_num):

    N, M, K = map(int,input().split())
    base_list = []
    temp_arr = []
    result_list = []
    

    for i in range(N):
        base_list.append(list(map(int,input().split())))


    # print(OuterSum(base_list))
    
    

    for i in range(N-K+1):      # 기본 보드에서 만들어질수 있는 모든 K*K크기의 정사각형을 temp_arr에 저장하여 조사
        for j in range(M-K+1):
            for n in range(K):
                temp_arr.append(base_list[i+n][j:j+K])
            result_list.append(OuterSum(temp_arr))
            temp_arr = []           
        
    result = max(result_list)
    
    print('#' + str(t+1) + ' ',end='')
    print(result)
