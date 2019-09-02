w, h = map(int,input().split())
p, q = map(int,input().split())

t = int(input())


def antMove(p,q,t):
    dw = (p + t) % (2*w)
    dh = (q + t) % (2*h)

    if dw <= w:
        p_result = dw
    else:                     # dw <= 2w
        p_result = (2 * w) - dw

    if dh <= h:
        q_result = dh
    else:                     # dw <= 2w
        q_result = (2 * h) - dh
    
    return [p_result, q_result]

    

    # if w - p > dw:
    #     p_result = p + dw
    # elif dw > (w - p) + w:
    #     p_result = abs((2 * w) - (p + dw))
    # else:
    #     p_result = (2 * w) - (p + dw)
    
    # if h - q > dh:
    #     q_result = q + dh
    # # elif dh > (h - p) + h:
    # #     q_result = q + dh
    # else:
    #     q_result = (2 * h) - (q + dh)

    # return [p_result, q_result]

print(' '.join(map(str,antMove(p,q,t))))
    