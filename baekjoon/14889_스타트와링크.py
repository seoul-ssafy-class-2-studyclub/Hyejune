N = int(input())
num = N//2
info = [0]*N
result_list = []
for i in range(N):
    info[i] = list(map(int,input().split()))

def combi(k,arr,now,su):
    if k == num:
        result_list.append(su)
        return
    else:
        for i in range(now+1, N):
            temp = su
            if now != -1:
                for j in range(len(arr)):
                    temp += info[arr[j]][i] + info[i][arr[j]]
            combi(k+1,arr+[i],i,temp)

combi(0,[],-1,0)
gap = 999
for i in range(len(result_list)//2):
    temp = abs(result_list.pop()-result_list.pop(0))
    if temp < gap:
        gap = temp
    if gap == 0:
        break

print(gap)


