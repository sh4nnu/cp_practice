q = int(input())
for i in range(q):
    c = 0
    a = int(input())
    if( a == 1):
        print(0)
    else:    
        while(a != 1):
            if(a % 2 == 0):
                a = a // 2
                c += 1
            elif( a % 3 == 0):
                a = 2*(a // 3)
                c += 1
            elif( a % 5 == 0):
                a = 4 * (a // 5)
                c += 1
            else:
                c = -1
                break
        print(c)
