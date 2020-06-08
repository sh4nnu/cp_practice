def findClosest(k, n, m):
    if(abs(k-n) >= abs(k-m)):
        return m
    else:
        return n

if __name__ == "__main__":
    t = int(input())
    for a in range(t):
        n,k = list(map(int, input().split()))
        l = list(map(int, input().split()))
        f=False
        if(k <= l[0]):
            f=True
            print(l[0])
            
        if(k>=l[n-1]):
            f=True
            print(l[n-1])
            

        i = 0; j = n; mid=0
        while(i<j and f==False):
            mid = (i+j)//2
            
            if(l[mid]==k):
                f=True
                print(k)
                break

            if(k<l[mid]):
                if(mid>0 and k > l[mid-1]):
                    f=True
                    print(findClosest(k,l[mid-1],l[mid]))
                    break
                j=mid

            else:
                if(mid < n-1 and k < l[mid+1]):
                    f=True
                    print(findClosest(k,l[mid],l[mid+1]))
                    break

                i=mid+1
        if(f==False):
            print(l[mid])