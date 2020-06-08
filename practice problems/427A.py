n = int(input())
l = list(map(int, input().split()))
crimes=0
hire=0
for x in l:
    if(x>0):
        hire+=x
    if(x<0):
        crimes+=1
    if(x<0 and hire > 0):
        hire-=1
        crimes-=1
print(crimes)
