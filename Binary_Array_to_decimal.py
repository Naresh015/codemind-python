n=int(input())
x=[int(i) for i in input().split()]
n=len(x)-1
t=0
for j in (x):
    t=t+int(j)*pow(2,n);
    n=n-1
print(t)