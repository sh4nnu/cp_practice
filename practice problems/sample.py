n = int(input())
A = list(map(int, input().split()))

for i in range(0,n,2):
    if(i<n-1):
        A[i],A[i+1] = A[i+1], A[i]
print(A)