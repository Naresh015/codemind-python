a=int(input())
if(a<3):
    print("The pattern is not possible")
else:
    for i in range(1,a+1): 
        for j in range(i): 
            print("*",end="")
        print()
    for i in reversed(range(a)): 
        if(i!=0):
            for j in range (i):
                print("*",end="")
            print()