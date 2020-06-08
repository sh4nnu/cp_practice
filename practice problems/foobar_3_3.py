def bfs(n):
    que = []
    dis ={}
    dis[n] = 0
    que.append(n)
    s={n}
    while(len(que)!=0):
        p = que.pop(0)
        if(p==1):
            break
        if((p-1) not in s):
            que.append(p-1)
            dis[p-1]=dis[p]+1
            s.add(p-1)
        if((p+1) not in s):
            que.append(p+1)
            dis[p+1]=dis[p]+1
            s.add(p+1)
        if(p%2==0):
            que.append(p/2)
            if((p/2) not in s):
                dis[p/2]=dis[p]+1
                s.add(p/2)
    return dis[1]
def solution(n):
    n = int(n)
    return bfs(n)

if __name__ == "__main__":
    n = int(input())
    l = solution(n)
    print l
