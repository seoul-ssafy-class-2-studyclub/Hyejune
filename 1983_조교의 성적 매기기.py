# test_case_num = int(input())
grade_dict = {0: 'A+', 1: 'A', 2: 'A-', 3: 'B+', 4: 'B', 5: 'B-', 6: 'C+', 7: 'C', 8: 'C-', 9: 'D'}
test_case_num = int(input())

for i in range(test_case_num):
    students_num = int(input())
    student_index = int(input())
    base_list = []
    result_list = []

    for i in range(students_num):
        base_list.append(str(input()).split())

    for i in range(students_num):
        su = 0
        su = int(base_list[i][0]) * 0.35 + int(base_list[i][1]) * 0.45 + int(base_list[i][2]) * 0.2
        result_list.append(su)

    target = result_list[student_index-1]   # 코드에서는 인덱스가 0부터 시작이므로

    # print(base_list)
    # print(result_list)
    # print(target)

    result_list.sort()
    result_list.reverse()
    # print(result_list)

    rank = result_list.index(target) // ( students_num / 10 )

    print('#' + (i+1) + ' ' + grade_dict[rank])

