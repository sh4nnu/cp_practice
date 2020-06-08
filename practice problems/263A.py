l=[]
x=0
y=0
for i in range(5):
    l = list(map(int, input().split()))
    y+=1
    if(l.count(1)==1):
        break
x = l.index(1)


print(abs(x-2)+abs(y-3))
