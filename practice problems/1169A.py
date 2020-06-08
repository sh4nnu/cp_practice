l = list(map(int,input().strip().split()))

point = [l[1],l[3]]
# print(point)

while((point[0] != l[2]) and (point[1] != l[4]) and (point[1] != point[0])):
    point[0] += 1
    point[1] -= 1

    if(point[0] == l[0]+1):
        point[0] = 1
    if(point[1] == 0):
        point[1] = l[0]
    # print(point)

if(point[0] == point[1]):
    print("YES")
else:
    print("NO")        

