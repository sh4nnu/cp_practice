n = int(input())
for x in range(n):
    num = int(input())
    strnum = str(num)
    l = len(strnum)
    numbers = []
    isround = False
    if(num % (10**(l-1)) ==0):
        isround = True
        
    i = 1
    while(isround == False and i < l):
        t = num%(10**i)
        if(t!=0):
            numbers.append(t)
            num -=t
        i+=1
        if(num % (10**(l-1)) ==0):
            isround = True
    numbers.append(num)
    print(len(numbers))
    for j in numbers:
        print(j, end =" ")
    print()
