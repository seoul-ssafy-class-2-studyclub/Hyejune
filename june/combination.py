# 조합은 now 변수 인자로 받기(맨 처음에 -1)
sample_list = ['a', 'b', 'c', 'd']

N = int(input())    # 몇개 뽑을지

result_list = []

def combination(k, arr, now):
    if k == N:
        result_list.append(arr)
    else:
        for i in range(now+1, len(sample_list)):
            combination(k+1, arr + [sample_list[i]], i)

combination(0,[],-1)
print(result_list)