# base_list = ['{', '}', '(', ')']

def check_bracket(arr):
    stack = []
    for item in arr:
        if item == '(' or item == '{':
            stack.append(item)
        elif item == ')':
            if stack == []:
                return 0
            elif stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif item == '}':
            if stack == []:
                return 0
            elif stack[-1] == '{':
                stack.pop()
            else:
                return 0
    if stack == []:       
        return 1
    else:
        return 0

test_num =int(input())

for t in range(test_num):
    test_case = list(input())
    # new_list = []
    # for item in test_case:
    #     if item in base_list:
    #         new_list.append(item)

    # print(new_list)

    result = check_bracket(test_case)

    print('#' + str(t+1) +' ', end='')
    print(result)

