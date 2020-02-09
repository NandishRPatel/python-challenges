def solution(array_a, array_b):
    total = 0
    for i,j in zip(array_a, array_b):
        total += (i - j) ** 2
    return total/len(array_a)