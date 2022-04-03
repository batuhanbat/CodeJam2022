def punched_carts(R, C):
    for r in range(2*R+1):
        line = ""
        for c in range(2*C+1):
            if r == 0:
                if c == 0 or c == 1:
                    line += "."
                else:
                    if c % 2 == 0:
                        line += "+"
                    else:
                        line += "-"
            elif r == 1:
                if c == 0 or c == 1:
                    line += "."
                else:
                    if c % 2 == 0:
                        line += "|"
                    else:
                        line += "."
            else:
                if r % 2 == 0:
                    if c % 2 == 0:
                        line += "+"
                    else:
                        line += "-"
                else:
                    if c % 2 == 0:
                        line += "|"
                    else:
                        line += "."
        print(line)      

T = int(input())

for case in range(1, T + 1):
    R, C = map(int, input().split())    
    print('Case #{}:'.format(case))
    punched_carts(R, C)
