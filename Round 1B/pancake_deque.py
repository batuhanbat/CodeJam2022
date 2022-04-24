from collections import deque

def pancake_deque(D):
    queue = deque(D)    

    prev_level = 0
    num_of_customers_paying = 0

    while queue:
        if queue[-1] >= queue[0]: # right end >= left end 
            if queue[0] >= prev_level:
                num_of_customers_paying += 1
                prev_level = queue[0]
            queue.popleft()            
        else:
            if queue[-1] >= prev_level:
                num_of_customers_paying += 1
                prev_level = queue[-1]
            queue.pop()
            
    return num_of_customers_paying
    
T = int(input())

for case in range(1, T + 1):
    N = int(input().strip())   
    D = list(map(int, input().split()))

    result = pancake_deque(D)
    print('Case #{}: {}'.format(case, result))
