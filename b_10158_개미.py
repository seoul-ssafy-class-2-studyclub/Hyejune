w, h = map(int,input().split())
p, q = map(int,input().split())

t = int(input())

t = t%(w*h)


diretions = {1: (0, -1), 2:(0, 1), 3:(-1, 0), 4:(1, 0)}
dx = []
​
def move(y, x, z, d):
    dx, dy = diretions[d]
    ry = y + dy
    rx = x + dx
    if ry == 0 or ry == N -1 or rx == 0 or rx == N -1:
        z = z // 2
        d = aside[d]
​
    return (ry, rx, z, d) 

def antLocation(t):

