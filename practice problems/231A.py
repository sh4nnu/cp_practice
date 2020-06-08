n = int(input())
c=0
for i in range(n):
    l = list(map(int, input().split()))
    if(l.count(1)>1):
        c+=1
print(c)
