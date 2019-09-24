import math

n, m = map(int,input().split())
x, y =map(int,input().split())


if 0 <= x <= n and 0 <= y <= m:
    z = x + y
    a = min(x, y)
    b = max(x,y)

    temp_res01 = 1
    temp_z = z
    for i in range(a):
        temp_res01 = temp_res01 * temp_z
        temp_z -= 1

    temp_res02 = math.factorial(a)
    print(z)
    print(temp_res01//temp_res02)
else:
    print('fail')