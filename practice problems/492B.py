n,l = list(map(int, input().split()))

street = list(map(int, input().split()))
street.sort()
maxdist = 0
maxdist = max(street[0], (l-street[n-1]))*2

for i in range(n-1):
    t = street[i+1] - street[i]
    if(maxdist < t):
        maxdist = t

print(maxdist/2)