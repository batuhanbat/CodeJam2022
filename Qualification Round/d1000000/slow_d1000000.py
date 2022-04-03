def d1000000(N, S):   

    longest_straight = 0
    if N <= 4:
        return N

    if N == 5:
        if max(S) >= N:
            return N
        else:
            return N-1

    for i in range(0,4):
        curr_min = min(S)
        curr_min_index = S.index(curr_min)
        del S[curr_min_index]

    longest_straight = 4

    i = 4
    while i < N:
        if len(S) != 0:
            if min(S) >= i+1:
                min_index = S.index(min(S))
                del S[min_index]
                longest_straight += 1
                i += 1
            else:
                min_index = S.index(min(S))
                del S[min_index]
                continue
        else:
            break            
    
    return longest_straight


T = int(input())

for case in range(1, T + 1):
    N = int(input().strip())   
    S = list(map(int, input().split()))

    result = d1000000(N,S)
    print('Case #{}: {}'.format(case, result))
    
