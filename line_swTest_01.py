num, c = map(int,input().split())

consumer = [[] for i in range(10)]
consumer_len = [101 for i in range(10)]

time_list = []
for i in range(num):
    time_list.append(int(input()))

# print(num, c, time_list)
# print(consumer)

cnt = 0

while cnt < c:
    consumer[cnt].extend(cnt+1 for i in range(time_list[cnt]))
    consumer_len[cnt] = time_list[cnt]
    cnt += 1

while cnt < num:    # 길이가 제일 짧은 리스트에 extend 시키기
    temp_current = consumer_len.index(min(consumer_len))
    consumer[temp_current].extend(cnt+1 for i in range(time_list[cnt]))
    consumer_len[temp_current] += time_list[cnt]
    cnt += 1


# print(consumer)
# print(consumer_len)

max_res = 0
for i in range(10):
    if consumer_len[i] != 101 and consumer_len[i] > max_res:
        max_res = consumer_len[i]

print(max_res)