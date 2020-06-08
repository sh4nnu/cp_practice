s = input()
test = "hello"
if(len(s) < 5):
    print("NO")
elif(len(s) == 5):
    if(s == "hello"):
        print("YES")
    else:
        print("NO")
else:
    i,j = 0,0
    while(i < len(s) and j < 5):
        if(s[i] == test[j]):
            j+=1
        i+=1
    if(j == 5):
        print("YES")
    else:
        print("NO")   
        
        