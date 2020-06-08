n,h = list(map(int, input().split()))
a  = list(map(int, input().split()))

min_width = 0
for x in a:
    if(x <= h):
        min_width += 1
    else:
        min_width+=2
print(min_width)