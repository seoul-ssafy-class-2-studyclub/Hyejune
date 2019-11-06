N = int(input())

cost_list = []
for i in range(N):
    cost_list.append(int(input()))

min_result = 999999

def my_func(idx, sum_cost, pre_move):
    global min_result
    if idx == N-1:
        if min_result > sum_cost:
            min_result = sum_cost
        return
    else:
        for i in range(2):
            if i == 0:  # 양의 방향으로 이동    
                current_move = pre_move + 1
                next_idx = idx + current_move
                if next_idx <= N-1:
                    my_func(next_idx, sum_cost + cost_list[next_idx], current_move)
            else:       # 음의 방향으로 이동
                next_idx = idx - pre_move
                if next_idx >= 0:
                    my_func(next_idx, sum_cost + cost_list[next_idx], pre_move)

my_func(2, cost_list[0] + cost_list[1], 1)

print(min_result)
