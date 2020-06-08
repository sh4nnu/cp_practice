def solution(times, time_limit):
    print times
    print time_limit
    n = len(times)
    safe_points=[]
    for i in range(n):
        for j in range(n):
            if(times[i][j]< 0):
                safe_points.append([i,j,times[i][j]])
    print "safe points:"
    print safe_points
    bunnies = []
    curr = 0
    isopen = True
    while(isopen):
        next = times[curr][:curr]+times[curr][curr+1:]
        print next
        isopen=False
    print "time up"
    return "WIP"

if __name__ == "__main__":
    n = int(input())
    times=[]
    for i in range(n):
        t = list(map(int, raw_input().split()))
        times.append(t)
    time_limit = int(input())
    l = solution(times, time_limit)
    print(l)
