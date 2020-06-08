s, n = list(map(int, input().split()))
dragos=[]
for t in range(n):
    l = list(map(int, input().split()))
    dragos.append(l)    
final=True
for i in sorted(dragos):
    if(s>i[0]):
        s+=i[1]
    else:
        final = False
        break
    
if(final):
    print("YES")
else:
    print("NO")