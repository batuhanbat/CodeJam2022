def double_or_not(S):
    return_string = ""
    for elem in S[::-1]:
        return_string = min(elem + return_string, elem + elem + return_string)
    return return_string

# I/O Code
T = int(input())
for case in range(1, T + 1):   
    S = str(input().strip())
    result = double_or_not(S)
    print('Case #{}: {}'.format(case, result))
