n = int(input())
l = list(map(int, input().split()))
a = 0
b = 0
for i in range(n):
    if(l[-1]>l[0]):
        val = l[-1]
        l=l[:-1]
    else:
        val=l[0]
        l=l[1:]
    if(i%2 == 0):
        a+=val
    else:
        b+=val

print(a,b)
