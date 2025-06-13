def solution(N):
    binary_str = bin(N)[2:]
    current_gap = 0
    max_gap = 0

    for digit in binary_str:
        if digit == '0':
            current_gap += 1 #curent gap = current gap + 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
    return max_gap


