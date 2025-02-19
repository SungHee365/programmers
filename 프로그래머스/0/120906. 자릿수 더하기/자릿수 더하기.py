def solution(n):
    n = list(str(n))
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum