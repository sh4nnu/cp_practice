def XORrow(begin, size):
    head = 0
    tail = 0
    n=size
    if(size == 0):
        return 0
    elif (size ==1):
        return begin
    elif (size == 2):
        return begin ^ begin+1
    else:
        if(begin&1):
            head = begin
            size-=1
        if(size&1):
            tail = begin + n-1 
            size-=1
        parity = 1 if (size %4) else 0
        return head ^ parity ^ tail        
        
def solution(start,length):
    a =start
    s = 0
    for i in range(length):
        s=s^XORrow(a, length-i)
        a=start+((i+1)*length)
    return s
if __name__ == "__main__":
    start = int(input())
    length = int(input())
    l = solution(start,length)
    print l
