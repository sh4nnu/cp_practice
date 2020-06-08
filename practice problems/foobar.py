def index(h, x):
    root = 2**h - 1
    parent = -1
    adjust = [0,0]
    while(x!=root):
        half=int(root/2)
        adjust[0] += adjust[1]
        adjust[1] = 0
        children = [half, root -1]
        if(x <= children[0]):
            parent = root
            root = children[0]
        else:
            x -= half
            adjust[1] = half
            parent = root
            root = children[1] - children[0]
    return parent + adjust[0]
def generate(h, q):
    s =[]
    for x in q:
        s.append(index(h,x))
    return s



if __name__ == "__main__":
    n = 3
    l = [7,3,5,1]
    t = len(l)
    l = generate(n,l)
    print l
