
a = [1, 1, 2, 3, 3, 6, 7, 9, 9]
b = [1, 2, 2, 3, 8, 9, 9, 9]

def listIntersection(a, b):
    final_list = []

    a_mid_result = {}
    b_mid_result = {}

    for i in set(a):
        a_mid_result[i] = a.count(i)

    for i in set(b):
        b_mid_result[i] = b.count(i)

    for key, val in a_mid_result.items():
        if key in b_mid_result.keys():
            t = min(val, b_mid_result[key])
            for i in range(t):
                final_list.append(key)

    return final_list


def listUnion(a, b):
    final_list = []

    a_mid_result = {}
    b_mid_result = {}

    for i in set(a):
        a_mid_result[i] = a.count(i)

    for i in set(b):
        b_mid_result[i] = b.count(i)

    for key, val in a_mid_result.items():
        if key in b_mid_result.keys():
            t = max(val, b_mid_result[key])
            for i in range(t):
                final_list.append(key)
        else:
            for i in range(val):
                final_list.append(key)

    for key, val in b_mid_result.items():
        if not key in a_mid_result.keys():
            for i in range(val):
                final_list.append(key)

    return final_list

print(listIntersection(a, b))
print(listUnion(a, b))