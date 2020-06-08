t = int(input())
for a in range(t):
    n = int(input())
    l=list(map(int, input().split()))
    l.sort()
    c = 1
    i =n//2
    a=[0] * (n+1)
    a[i]=l[0]
    while(c<n):
        if(c%2==0):
            i-=c
        else:
            i+=c
        print(i,c)
        a[i] = l[c]
        c+=1
    if(n%2==0):
        a=a[1:]
    else:
        a=a[:-1]
    print(a)