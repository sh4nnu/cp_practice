import math
n = int(input())
factors =[]
for i in range(1,int(math.sqrt(n))+1):
    if(n%i == 0):
        if(n//i == i):
            factors.append(i)
        else:
            factors.append(i)
            factors.append(n//i)
print(len(factors))