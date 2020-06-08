def solution(src,dest):
    class cell:
        def __init__(self, x=0,y=0,dist=0):
            self.x = x
            self.y= y
            self.dist= dist
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
    origin = cell(src//8,src%8,0)
    target = [dest//8, dest%8]
    que = []
    visited = [[False for i in range(9)] for j in range(9)]
    que.append(origin)
    visited[src//8][src%8] = True
    while(len(que)!=0):
        t = que.pop(0)
        if(t.x == target[0] and t.y == target[1]):
            return t.dist
        for i in range(8):
            a = t.x+dx[i]
            b = t.y+dy[i]
            if((a >=0 and a<=8) and (b>=0 and b<=8) and not visited[a][b]):
                visited[a][b] = True
                que.append(cell(a,b,t.dist+1))


if __name__ == "__main__":

    l = solution(0,1)
    print l
