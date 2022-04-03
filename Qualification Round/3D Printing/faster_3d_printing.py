def printing(printer1,printer2,printer3):

    all_c_list = []
    all_m_list = []
    all_y_list = []
    all_k_list = []

    all_c_list.append(printer1[0])
    all_c_list.append(printer2[0])
    all_c_list.append(printer3[0])

    all_m_list.append(printer1[1])
    all_m_list.append(printer2[1])
    all_m_list.append(printer3[1])

    all_y_list.append(printer1[2])
    all_y_list.append(printer2[2])
    all_y_list.append(printer3[2])

    all_k_list.append(printer1[3])
    all_k_list.append(printer2[3])
    all_k_list.append(printer3[3])

    min_c = min(all_c_list)
    min_m = min(all_m_list)
    min_y = min(all_y_list)
    min_k = min(all_k_list)
   
    total = min_c + min_m + min_y + min_k

    if total < 1000000 :
        return None

    elif total == 1000000:
        return [min_c, min_m, min_y, min_k]
    
    L = [min_c, min_m, min_y, min_k]

    extra_total = total - 1000000
    while extra_total > 0:
        stop = False
        for i in range(0,4):
            if extra_total > 0:
                if L[i] > 1:
                    L[i] -= 1
                    extra_total -= 1
            else:
                stop = True
                break
        if stop == True:
            break    

    return L

# I/O Code
T = int(input())

for case in range(1, T + 1):
    printer1 = []
    printer2 = []
    printer3 = []
    for i in range(3):        
        C , M , Y , K = map(int, input().split())   
        if i == 0:     
            printer1.append(C)
            printer1.append(M)
            printer1.append(Y)
            printer1.append(K)
        elif i == 1:
            printer2.append(C)
            printer2.append(M)
            printer2.append(Y)
            printer2.append(K)
        elif i == 2:
            printer3.append(C)
            printer3.append(M)
            printer3.append(Y)
            printer3.append(K)        

    L = printing(printer1,printer2,printer3)  
    result = "IMPOSSIBLE" if L is None else " ".join(map(str, L))
    print('Case #{}: {}'.format(case, result))
