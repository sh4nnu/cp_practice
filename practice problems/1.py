n = int(input())
l = list(map(int, input().split()))
d = []
l.sort()
s = set(l)
if(len(l) == len(s)):
    print("Amith")
else:
    for x in l:
        if(l.count(x) >1):
            d.append(x)
    ds = set(d)
    if(len(ds)>1):
        print("Amith")
    else:
        print("Amruth") # this gives the else output.
