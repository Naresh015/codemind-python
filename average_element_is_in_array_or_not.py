n=int(input())
a=list(map(int,input().split()))
b=int(sum(a)/n)
if b in a:
    print("True")
else:
    print("False")
