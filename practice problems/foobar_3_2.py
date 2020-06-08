def solution(n):
    size = n
    if(n==3 or n==4):
        return 1
    else:
        dparr=[[0 for i in range(n+1)] for j in range(n+1)]
        dparr[3][2] = 1
        dparr[4][2] = 1
        for i in range(5,n+1):
            for k in range(2, i+1):
                if(k == 2):
                    dparr[i][k] = dparr[i-k][k]+1
                else:
                    dparr[i][k] = dparr[i-k][k] + dparr[i-k][k-1]
        ans =0
        for j in range(1, n+1):
            ans+=dparr[n][j]
    return ans
    


if __name__ == "__main__":
    n = int(input())
    l = solution(n)
    print l
