def d1000000(N, S):   

    if N <= 4:
        return N

    if N == 5:
        if max(S) >= N:
            return N
        else:
            return N-1

    longest_straight = 0

    
    countmap = {}
    for s in S:
        if s in countmap.keys():
            countmap[s] += 1
        else:
            countmap[s] = 1

    uniques_list = list(dict.fromkeys(S))
    reverse_sorted = sorted(uniques_list, reverse=True )

    for i in range(0,4):
        curr_min = reverse_sorted[len(reverse_sorted)-1]
        
        countmap[curr_min] -= 1
        if countmap[curr_min] == 0:
            del countmap[curr_min]
            reverse_sorted.pop()

        longest_straight += 1  

    i = 4
    while i < N:
        if len(countmap) != 0:
            if reverse_sorted[len(reverse_sorted)-1] >= i+1:
                minnn = reverse_sorted[len(reverse_sorted)-1]
                countmap[minnn] -= 1
                if countmap[minnn] == 0:
                    del countmap[minnn]
                    reverse_sorted.pop()
                longest_straight += 1
                i += 1
            else:
                minn = reverse_sorted[len(reverse_sorted)-1]
                countmap[minn] -= 1
                if countmap[minn] == 0:
                    del countmap[minn]
                    reverse_sorted.pop()
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
