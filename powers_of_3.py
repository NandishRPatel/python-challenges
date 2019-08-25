def largestPower(N):
    i = 0
    final_list = []
    while True:
        if 3 ** i < N:
            final_list.append(i)
        else:
            break
        i += 1
    if len(final_list) == 0: return -1
    else:return max(final_list)